from __future__ import annotations

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import build_add_question_form
from .models import CustomQuestions, Theme


class NewQuestion(LoginRequiredMixin, FormView):
    """
    Добавление вопросов от пользователя
    """

    template_name = "pages/questions/new_question.html"
    success_url = reverse_lazy("questions:new")

    @property
    def form_class(self):
        """
        Генерация динамической формы, добавленией ей атрибутов
        """

        form = build_add_question_form()
        form.declared_fields["Тема вопроса"].widget.attrs = {
            "class": "form-control",
            "placeholder": "Тема вопроса",
        }
        form.declared_fields["Вопрос"].widget.attrs = {
            "class": "form-control",
            "placeholder": "Текст вопроса",
        }
        return form

    @property
    def form_class(self):
        """
        Coздаём динамическую форму для вьюшки
        """
        return build_create_interview_form()


    def form_valid(self, form) -> HttpResponseRedirect:  # noqa: F821
        """
        Сохранение нового вопроса
        """

        new_user_question = CustomQuestions()
        new_user_question.user = self.request.user
        new_user_question.text = form.cleaned_data["Вопрос"]
        new_user_question.answer = form.cleaned_data["Ответ"]
        new_user_question.theme = Theme.objects.get(
            pk=int(form.cleaned_data["Тема вопроса"])
        )
        new_user_question.save()
        messages.success(self.request, "Ваш вопрос сохранен.")

        return super().form_valid(form)
