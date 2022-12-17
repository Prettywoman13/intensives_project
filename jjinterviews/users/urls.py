from django.contrib.auth.views import (LoginView, LogoutView,
                                       PasswordChangeDoneView,
                                       PasswordChangeView,
                                       PasswordResetCompleteView,
                                       PasswordResetConfirmView,
                                       PasswordResetDoneView,
                                       PasswordResetView)
from django.urls import path, reverse_lazy
from users.forms import (CustomPasswordResetConfirmForm,
                         CustomPasswordResetForm, PasswordChangeForm,
                         UserLoginForm)
from users.views import ProfileView, RegisterView

app_name = "users"

urlpatterns = [
    path(
        "login/",
        LoginView.as_view(
            template_name="pages/users/login.html",
            authentication_form=UserLoginForm,
        ),
        name="login",
    ),
    path(
        "logout/",
        LogoutView.as_view(
            template_name="pages/users/logged_out.html",
        ),
        name="logout",
    ),
    path(
        "password_change/",
        PasswordChangeView.as_view(
            template_name="pages/users/password_change.html",
            form_class=PasswordChangeForm,
            success_url=reverse_lazy("users:password_change_done"),
        ),
        name="password_change",
    ),
    path(
        "password_change/done/",
        PasswordChangeDoneView.as_view(
            template_name="pages/users/password_change_done.html"
        ),
        name="password_change_done",
    ),
    path(
        "password_reset/",
        PasswordResetView.as_view(
            template_name="pages/users/password_reset.html",
            form_class=CustomPasswordResetForm,
            success_url=reverse_lazy("users:password_reset_done"),
        ),
        name="password_reset",
    ),
    path(
        "password_reset/done/",
        PasswordResetDoneView.as_view(
            template_name="pages/users/password_reset_done.html",
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(
            template_name="pages/users/password_reset_confirm.html",
            form_class=CustomPasswordResetConfirmForm,
            success_url=reverse_lazy("users:password_reset_complete"),
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        PasswordResetCompleteView.as_view(
            template_name="pages/users/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    path("register/", RegisterView.as_view(), name="register"),
    path("profile/<pk>", ProfileView.as_view(), name="profile"),
]
