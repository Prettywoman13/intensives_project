from django.db import models

from .managers import SectionManger, QuestionManager, ThemeManager


class Section(models.Model):
    name = models.CharField(max_length=70)

    objects = SectionManger()

    class Meta:
        verbose_name = "раздел"
        verbose_name_plural = "разделы"

    def __str__(self) -> str:
        return self.name


class Theme(models.Model):
    name = models.CharField(max_length=70)
    section = models.ForeignKey(
        'Section', on_delete=models.CASCADE, related_name="theme"
    )

    objects = ThemeManager()

    class Meta:
        verbose_name = "тема"
        verbose_name_plural = "темы"

    def __str__(self) -> str:
        return self.name


class Question(models.Model):
    theme = models.ForeignKey(
        Theme, on_delete=models.CASCADE, related_name="question"
    )
    text = models.CharField(max_length=200)
    answer = models.TextField()

    objects = QuestionManager()

    def __str__(self) -> str:
        return f"{self.theme}: {self.text}"

    class Meta:
        verbose_name = "вопрос"
        verbose_name_plural = "вопросы"
