from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.mail import send_mail
from django.db import models
from django.utils.translation import gettext_lazy as _
from users.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("почта"), unique=True, blank=False)
    password = models.CharField(_("пароль"), max_length=128)
    avatar = models.ImageField(_("аватар"))
    username = models.CharField(_("имя"), max_length=50, blank=True)
    date_joined = models.DateTimeField(
        _("дата регистрации"), auto_now_add=True
    )
    is_active = models.BooleanField(_("активный"), default=True)
    is_staff = models.BooleanField(
        _("staff status"),
        help_text=_(
            "Designates whether the user can log into this admin site."
        ),
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
        return self.username

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Отправляет письмо пользователю.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)
