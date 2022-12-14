from django import forms
from django.contrib.auth.forms import (AuthenticationForm, PasswordChangeForm,
                                       PasswordResetForm, SetPasswordForm,
                                       UserChangeForm, UserCreationForm)

from users.models import User


class CustomUserCreationForm(UserCreationForm):
    """
    Форма создания пользователя
    """

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields["password1"].label = "Пароль"
        self.fields["password2"].label = "Повторите пароль"
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"
            visible.field.widget.attrs["placeholder"] = visible.field.label

    class Meta:
        model = User
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("email",)


class UserLoginForm(AuthenticationForm):
    """
    Форма для авторизации пользователей.
    """

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Почта",
                "id": "Username",
                "type": "email",
                "aria-describedby": "emailHelp",
            }
        )
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Пароль",
                "type": "password",
                "id": "password",
            }
        ),
    )


class UserUpdateForm(forms.ModelForm):
    """
    Форма обновления пользователя.
    """

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = User
        fields = ("email", "avatar", "nickname")


class PasswordChangeForm(PasswordChangeForm):
    """
    Форма смены пароля.
    """

    def __init__(self, *args, **kwargs):
        super(PasswordChangeForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"
            field.field.widget.attrs["type"] = "password"
            field.field.widget.attrs["id"] = "form3Example4cg"


class CustomPasswordResetForm(PasswordResetForm):
    """
    Форма сброса пароля(1)
    """

    def __init__(self, *args, **kwargs):
        super(CustomPasswordResetForm, self).__init__(*args, **kwargs)
        self.fields["email"].widget.attrs.update({"class": "form-control"})


class CustomPasswordResetConfirmForm(SetPasswordForm):
    """
    Форма сброса пароля(2)
    """

    def __init__(self, *args, **kwargs):
        super(CustomPasswordResetConfirmForm, self).__init__(*args, **kwargs)
        self.fields["new_password1"].widget.attrs.update(
            {"class": "form-control"}
        )
        self.fields["new_password2"].widget.attrs.update(
            {"class": "form-control"}
        )
