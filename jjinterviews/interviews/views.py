from random import choice

from django.core.paginator import Paginator
from django.shortcuts import redirect, render, reverse
from django.views.generic import FormView

from questions.models import Question
from .forms import build_create_interview_form
from .models import Interview, Pack


class CreateInterview(FormView):
    template_name = "pages/interviews/create.html"

    @property
    def form_class(self):
        return build_create_interview_form()

    def form_valid(self, form):
        email_interviewed = form.cleaned_data.pop("Почта")
        ids_list = [
            int(id) for sublist in form.cleaned_data.values() for id in sublist
        ]
        new_pack = Pack()
        new_pack.save()

        questions = (
            Question.objects.all().filter(theme__in=ids_list).order_by("theme")
        )
        questions_iter = iter(questions)
        first = next(questions_iter)
        first_id = 0
        curr_theme = first.theme
        for i, question in enumerate(questions_iter, start=1):
            if curr_theme != question.theme:
                new_pack.questions.add(choice(questions[first_id:i]))
                first_id = i
                curr_theme = question.theme

        new_pack.questions.add(choice(questions[first_id:]))

        new_interview = Interview(
            pack_id=new_pack,
            user_id=self.request.user,
            email_interviewed=email_interviewed,
        )
        new_interview.save()
        return redirect(
            reverse(
                "interviews:interview",
                kwargs={"interview_id": new_interview.id},
            )
        )


def interview_view(request, interview_id):
    interview = Interview.objects.get(pk=interview_id)
    pack = interview.pack_id
    questions = pack.questions.all()
    contact_list = questions
    paginator = Paginator(contact_list, 1)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request, "pages/interviews/interview.html", {"page_obj": page_obj}
    )
