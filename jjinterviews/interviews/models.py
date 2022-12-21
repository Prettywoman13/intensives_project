import uuid

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from core.models import BelongUserMixin, InterviewedEmailMixin
from questions.models import Question

from .managers import QuestionStatisticManager


class Pack(models.Model):
    questions = models.ManyToManyField(Question)


class Interview(BelongUserMixin, InterviewedEmailMixin, models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pack = models.ForeignKey("Pack", on_delete=models.PROTECT)
    closed = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Собеседование"
        verbose_name_plural = "Собеседования"


class QuestionStatistic(BelongUserMixin, InterviewedEmailMixin, models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    interview = models.ForeignKey(Interview, on_delete=models.DO_NOTHING)
    mark = models.IntegerField(null=True)

    objects = QuestionStatisticManager()


class InterviewStatistic(BelongUserMixin, InterviewedEmailMixin):
    interview = models.ForeignKey(Interview, on_delete=models.DO_NOTHING)
    completion_percentage = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(1.0)], null=True
    )
