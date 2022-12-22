from __future__ import annotations

from django.db import models


class QuestionStatisticManager(models.Manager):
    def get_not_null_stats(self, interview) -> list[Interview]:  # noqa: F821
        """
        Получение всех отвеченных вопросов по интервью
        """
        return self.get_queryset().filter(
            interview=interview, mark__isnull=False
        )

    def get_all_stats(self, interview) -> list[Interview]:  # noqa: F821
        """
        Получение всех всех вопросов по интервью
        """
        return self.get_queryset().filter(
            interview=interview
        )
