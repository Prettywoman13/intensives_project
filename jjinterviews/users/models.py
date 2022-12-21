from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.mail import send_mail
from django.db import models

from users.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(("почта"), unique=True, blank=False)
    password = models.CharField(("пароль"), max_length=128)
    avatar = models.ImageField(("аватар"), blank=True)
    nickname = models.CharField(("имя"), max_length=50, blank=True)
    date_joined = models.DateTimeField(
        ("дата регистрации"), auto_now_add=True
    )
    is_active = models.BooleanField(("активный"), default=True)
    is_staff = models.BooleanField(
        ("staff status"),
        default=False,
        help_text=("Moderator"),
    )

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = ("пользователь")
        verbose_name_plural = ("пользователи")

    def get_short_name(self):
        """
        Возвращает имя пользователя.
        """
        return self.nickname

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Отправляет письмо пользователю.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)
