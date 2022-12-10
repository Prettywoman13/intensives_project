from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.mail import send_mail
from django.db import models
from django.utils.translation import gettext_lazy as _
from users.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()
    email = models.EmailField(_("почта"), unique=True, blank=False)
    password = models.CharField(_("пароль"), max_length=128)
    avatar = models.ImageField(_("аватар"))
    first_name = models.CharField(_("имя"), max_length=30, blank=True)
    date_joined = models.DateTimeField(
        _("дата регистрации"), auto_now_add=True
    )
    is_active = models.BooleanField(_("активный"), default=True)
    is_staff = models.BooleanField(
        _("персонал"),
        default=False,
    )
    birthday = models.DateField(
        verbose_name="день рождения", null=True, blank=True
    )

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("пользователь")
        verbose_name_plural = _("пользователи")

    def get_short_name(self):
        """
        возвращает имя пользователя.
        """
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Отправляет письмо пользователю.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)


class Intern(models.Model):
    interviewier = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="intern"
    )
    email = models.EmailField(_("почта"), unique=True, blank=False, null=False)

    class Meta:
        verbose_name = "стажёр"
        verbose_name_plural = "стажёры"
