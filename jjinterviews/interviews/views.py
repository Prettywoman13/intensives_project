from itertools import chain

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import redirect, render, reverse
from django.views.generic import FormView

from questions.models import Question

from .forms import build_create_interview_form
from .models import Interview, InterviewStatistic, QuestionStatistic
from .utils import create_pack


class CreateInterview(LoginRequiredMixin, FormView):
    template_name = "pages/interviews/create.html"

    @property
    def form_class(self):
        """
        Coздаём динамическую форму для вьюшки
        """
        return build_create_interview_form()

    def form_valid(self, form):
        """
        Генерируем вопросы на собеседование
        """
        email_interviewed = form.cleaned_data.pop("Почта")
        custom = form.cleaned_data.pop("Пользовательские вопросы")
        user_questions = []

        if not any(form.cleaned_data.values()):
            messages.warning(self.request, "Вы не выбрали темы вопросов")
            return redirect(self.request.META["HTTP_REFERER"])
        ids_list = [
            int(id) for sublist in form.cleaned_data.values() for id in sublist
        ]

        questions = (
            Question.objects.all()
            .filter(theme__in=ids_list, user=None)
            .order_by("theme")
        )
        if custom:
            user_questions = (
                Question.objects.all()
                .filter(theme__in=ids_list, user=self.request.user)
                .order_by("theme")
            )

        all_questions = chain(questions, user_questions)
        new_interview = Interview(
            pack=create_pack(list(all_questions)),
            user=self.request.user,
            email_interviewed=email_interviewed,
        )
        new_interview.save()

        new_interview_statistic = InterviewStatistic(
            interview=new_interview,
            user=self.request.user,
            email_interviewed=email_interviewed,
            completion_percentage=None,
        )
        new_interview_statistic.save()

        return redirect(
            reverse(
                "interviews:interview",
                kwargs={"interview_id": new_interview.id},
            )
        )


def interview_view(request, interview_id):
    """
    Тут было решено использовать FBV, а не CBV, для удобства разработки,
    в случае реализации классом, появилось бы много лишнего кода
    """

    interview = Interview.objects.prefetch_related("pack").get(pk=interview_id)

    questions = interview.pack.questions.all().order_by("theme")
    contact_list = questions

    paginator = Paginator(contact_list, 1)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    statistic_obj, created = QuestionStatistic.objects.get_or_create(
        question=page_obj[0],
        interview=interview,
        user=request.user,
        defaults={
            "question": page_obj[0],
            "interview": interview,
            "email_interviewed": interview.email_interviewed,
            "mark": None,
            "user": request.user,
        },
    )

    context = {
        "page_obj": page_obj,
        "range_default": statistic_obj.mark,
        "is_open": not interview.closed,
    }
    if request.method == "POST":
        if "rate" in request.POST:
            statistic_obj.mark = request.POST["rate"]
            statistic_obj.save()
            messages.success(
                request,
                "Оценка сохранена",
            )
        elif "close_interview" in request.POST:
            ids_list = [x.pk for x in interview.pack.questions.all()]
            questions_state = (
                QuestionStatistic.objects.all()
                .filter(interview=interview, question__in=ids_list, mark=None)
                .values(
                    "mark",
                )
            )
            if any(questions_state):
                messages.warning(
                    request,
                    (
                        "Вы не можете закончить собеседование пока "
                        "не поставили оценки на все вопросы"
                    ),
                )
                return redirect(request.META["HTTP_REFERER"])
            interview.closed = True
            interview.save()
            questions_stats = QuestionStatistic.objects.get_not_null_stats(
                interview
            )
            questions_count = len(questions_stats)
            if questions_count > 0:
                percent = (
                    sum(map(lambda obj: obj.mark / 2, questions_stats))
                    / questions_count
                )
                interview_statistic = InterviewStatistic.objects.get(
                    interview=interview
                )
                interview_statistic.completion_percentage = percent
                interview_statistic.save()
        return redirect(request.META["HTTP_REFERER"])

    return render(request, "pages/interviews/interview.html", context=context)
