from django.db import models


class QuestionStatisticManager(models.Manager):
    def get_stats_for_interview(self, interview) -> 'Interview':  # noqa 821
        """
        Получение статистики для собеса
        """
        return self.get_queryset().filter(
            interview=interview, mark__isnull=False
        )
