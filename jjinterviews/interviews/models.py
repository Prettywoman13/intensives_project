import uuid

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from core.models import BelongUserMixin, InterviewedEmailMixin
from questions.models import Question

from .managers import QuestionStatisticManager


class Pack(models.Model):
    """
    Пак вопросов - промежуточная сущность между
    собеседованием и всеми вопросами
    """

    questions = models.ManyToManyField(Question, verbose_name="вопросы")


class Interview(BelongUserMixin, InterviewedEmailMixin, models.Model):
    """
    Интервью - самая базовая сущность. uuid выбран,
    тк id используется в формировании юрла до собеса
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name="идентификатор",
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="время создания"
    )
    pack = models.ForeignKey(
        "Pack", on_delete=models.PROTECT, verbose_name="пак вопросов"
    )
    closed = models.BooleanField(
        default=False, verbose_name="статус открыто/закрыто"
    )

    class Meta:
        verbose_name = "Собеседование"
        verbose_name_plural = "Собеседования"


class QuestionStatistic(BelongUserMixin, InterviewedEmailMixin, models.Model):
    """
    Статистика вопросов
    """

    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, verbose_name="вопрос"
    )
    interview = models.ForeignKey(
        Interview, on_delete=models.DO_NOTHING, verbose_name="собеседование"
    )
    mark = models.IntegerField(null=True, verbose_name="оценка")

    objects = QuestionStatisticManager()


class InterviewStatistic(BelongUserMixin, InterviewedEmailMixin):
    """
    Статистика собесов
    """

    interview = models.ForeignKey(Interview, on_delete=models.DO_NOTHING)
    completion_percentage = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(1.0)],
        null=True,
        verbose_name="процент верных ответов",
    )
