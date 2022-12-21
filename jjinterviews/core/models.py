from django.db import models

from users.models import User


class InterviewedEmailMixin(models.Model):
    """
    Миксин, добавляющий почту человека, который проходит собеседование
    """

    email_interviewed = models.EmailField(max_length=80)

    class Meta:
        abstract = True


class BelongUserMixin(models.Model):

    """
    Миксин для сущностей, которыми обладает пользователь
    """

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    class Meta:
        abstract = True
