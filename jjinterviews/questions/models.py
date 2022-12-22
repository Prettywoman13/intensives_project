from django.db import models

from users.models import User


class Section(models.Model):
    """
    Секция вопроса, например: SQL, Django, основы Python
    """

    name = models.CharField(verbose_name="название", max_length=70)

    class Meta:
        verbose_name = "раздел"
        verbose_name_plural = "разделы"

    def __str__(self) -> str:
        return self.name


class Theme(models.Model):
    """
    Тема вопроса, например: Функции, ООП, Django orm
    """

    name = models.CharField(verbose_name="название", max_length=70)
    section = models.ForeignKey(
        "Section",
        on_delete=models.CASCADE,
        related_name="theme",
        verbose_name="категория",
    )

    class Meta:
        verbose_name = "тема"
        verbose_name_plural = "темы"

    def __str__(self) -> str:
        return self.name


class Question(models.Model):
    """
    Модель вопроса, также содержит и ответ на него
    """

    user = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
        verbose_name="пользователь",
    )

    theme = models.ForeignKey(
        "Theme",
        on_delete=models.CASCADE,
        related_name="question",
        verbose_name="тема",
    )
    text = models.CharField(max_length=200, verbose_name="вопрос")
    answer = models.TextField(verbose_name="ответ")

    def __str__(self) -> str:
        return f"{self.theme}: {self.text}"

    class Meta:
        verbose_name = "вопрос"
        verbose_name_plural = "вопросы"
