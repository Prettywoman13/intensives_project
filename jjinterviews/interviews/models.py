import uuid

from django.db import models

from core.models import InterviewedMixin
from questions.models import Question
from users.models import User


class Pack(models.Model):
    questions = models.ManyToManyField(Question)


class Interview(InterviewedMixin, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    pack = models.ForeignKey("Pack", on_delete=models.PROTECT)
    closed = models.BooleanField(default=False)


class QuestionStatistic(InterviewedMixin, models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    interview = models.ForeignKey(Interview, on_delete=models.DO_NOTHING)
    mark = models.IntegerField(null=True)
