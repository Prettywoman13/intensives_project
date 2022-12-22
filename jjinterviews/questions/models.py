from django.db import models


class Section(models.Model):
    """
    Секция вопроса, например: SQL, Django, основы Python
    """
    name = models.CharField(max_length=70)

    class Meta:
        verbose_name = "раздел"
        verbose_name_plural = "разделы"

    def __str__(self) -> str:
        return self.name


class Theme(models.Model):
    """
    Тема вопроса, например: Функции, ООП, Django orm
    """
    name = models.CharField(max_length=70)
    section = models.ForeignKey(
        "Section", on_delete=models.CASCADE, related_name="theme"
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
    theme = models.ForeignKey(
        "Theme", on_delete=models.CASCADE, related_name="question"
    )
    text = models.CharField(max_length=200)
    answer = models.TextField()

    def __str__(self) -> str:
        return f"{self.theme}: {self.text}"

    class Meta:
        verbose_name = "вопрос"
        verbose_name_plural = "вопросы"
