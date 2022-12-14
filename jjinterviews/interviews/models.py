from django.db import models

from core.models import InterviewedMixin
from questions.models import Question
from users.models import User


class Pack(models.Model):
    questions = models.ManyToManyField(Question)


class Interview(InterviewedMixin, models.Model):
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    pack_id = models.ForeignKey("Pack", on_delete=models.PROTECT)


class QuestionStatistic(InterviewedMixin, models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    interview_id = models.ForeignKey(Interview, on_delete=models.DO_NOTHING)
    mark = models.BooleanField()
