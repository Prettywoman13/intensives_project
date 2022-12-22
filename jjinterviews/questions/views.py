from __future__ import annotations

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import NewQuestionForm, build_create_interview_form


class NewQuestion(LoginRequiredMixin, FormView):
    """
    Добавление вопросов от пользователя
    """

    login_url = reverse_lazy("users:login")
    template_name = "pages/questions/new_question.html"
    success_url = reverse_lazy("questions:new_question")

    @property
    def form_class(self):
        """
        Coздаём динамическую форму для вьюшки
        """
        return build_create_interview_form()


    def form_valid(self, form) -> HttpResponseRedirect:  # noqa: F821
        form.save()
        messages.success(self.request, "Ваш вопрос сохранен.")
        return super().form_valid(form)
