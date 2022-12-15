from django.db import models


class InterviewedMixin(models.Model):
    """
    Миксин, добавляющий почту человека, который проходит собеседование
    """

    email_interviewed = models.EmailField(max_length=80)

    class Meta:
        abstract = True
