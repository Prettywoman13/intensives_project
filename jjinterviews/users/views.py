from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView

from users.forms import CustomUserCreationForm, UserUpdateForm
from users.models import User


class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    login_url = reverse_lazy("users:login")
    template_name = "pages/users/profile.html"

    def get_success_url(self) -> str:
        success_url = reverse_lazy(
            "users:profile", kwargs={"pk": self.request.user.id}
        )
        return success_url

    def get(self, request, *args: str, **kwargs):

        if request.user.id == int(kwargs["pk"]) or request.user.is_superuser:
            return super().get(request, *args, **kwargs)
        raise Http404


class RegisterView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = "pages/users/register.html"

    def get_success_url(self) -> str:
        success_url = reverse_lazy("users:login")
        return success_url
