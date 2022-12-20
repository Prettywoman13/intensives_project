from django.db import models


class QuestionStatisticManager(models.Manager):
    def get_stats_for_interview(self, interview):
        return self.get_queryset().filter(
            interview=interview, mark__isnull=False
        )
