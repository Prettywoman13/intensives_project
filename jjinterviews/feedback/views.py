from __future__ import annotations

from django.contrib import messages
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import FormView

from users.models import User

from .forms import FeedBackForm


class FeedBack(FormView):
    form_class = FeedBackForm
    template_name = "pages/feedback.html"
    success_url = reverse_lazy("feedback:main")

    def get_context_data(self, **kwargs) -> dict:
        """
        Получаем пользователя по емейлу, если он авторизован
        """
        kwargs["form"] = self.form_class(
            initial={"mail": self.request.user.email}
            if self.request.user.is_authenticated
            else {}
        )
        return super(FeedBack, self).get_context_data(**kwargs)

    def form_valid(self, form) -> HttpResponseRedirect:  # noqa: F821
        """
        Обрабатываем пришедшую форму,
        рассылаем всем админам обратную связь
        """
        text = form.cleaned_data["text"]
        mail = form.cleaned_data["mail"]
        send_mail(
            "Здравствуйте, админ. Вам пришла обратная связь.",
            text,
            mail,
            [user.email for user in User.objects.filter(is_superuser=True)],
            fail_silently=True,
        )
        form.save()
        messages.success(
            self.request, "Сообщение отправлено, мы вас очень ценим"
        )
        return super().form_valid(form)
