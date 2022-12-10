from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from users.models import User


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields["password1"].label = "пароль"
        self.fields["password2"].label = "пароль"
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"
            visible.field.widget.attrs["placeholder"] = visible.field.label

    class Meta:
        model = User
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm):
    def __init__(self, *args, **kwargs) -> None:
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)
        self.fields["password"].label = "пароль"

    class Meta:
        model = User
        fields = ("email",)
