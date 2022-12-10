from uuid import uuid4

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.mail import send_mail
from django.db import models
from django.utils.translation import gettext_lazy as _

from users.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    id = models.TextField(
        primary_key=True,
        default=uuid4,
        unique=True,
        editable=False,
    )
    email = models.EmailField(_("почта"), unique=True, blank=False)
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        null=False,
        blank=False,
        help_text=_(
            "Обязательно. 150 символов или меньше."
            "Только буквы, числа и @/./+/-/_"
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("Пользователь с таким никнеймом уже существует."),
        },
    )
    password = models.CharField(_("пароль"), max_length=128)
    avatar = models.ImageField(_("аватар"))
    first_name = models.CharField(_("имя"), max_length=30, blank=True)
    last_name = models.CharField(_("фамилия"), max_length=30, blank=True)
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

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """
        Returns the short name for the user.
        """
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)


class Intern(models.Model):
    interviewier = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="intern"
    )
    first_name = models.CharField(_("имя"), max_length=150, blank=True)
    last_name = models.CharField(_("фамилия"), max_length=150, blank=True)
    email = models.EmailField(_("почта"), unique=True, blank=False, null=False)
    date_joined = models.DateTimeField(
        _("дата регистрации"), auto_now_add=True
    )

    class Meta:
        verbose_name = "стажёр"
        verbose_name_plural = "стажёры"
