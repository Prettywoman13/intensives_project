from __future__ import annotations

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import NewQuestionForm


class NewQuestion(LoginRequiredMixin, FormView):
    """
    Добавление вопросов от пользователя
    """

    login_url = reverse_lazy("users:login")
    form_class = NewQuestionForm
    template_name = "pages/questions/new_question.html"
    success_url = reverse_lazy("questions:new_question")

    def form_valid(self, form) -> HttpResponseRedirect:  # noqa: F821
        form.save()
        messages.success(self.request, "Ваш вопрос сохранен.")
        return super().form_valid(form)
