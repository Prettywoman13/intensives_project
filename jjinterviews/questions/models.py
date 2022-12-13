from django.db import models


class Section(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self) -> str:
        return self.name


class Theme(models.Model):
    name = models.CharField(max_length=70)
    section = models.ForeignKey(
        Section, on_delete=models.CASCADE, related_name="theme"
    )

    def __str__(self) -> str:
        return self.name


class QuestionTheme(models.Model):
    theme = models.ForeignKey(
        Theme, on_delete=models.CASCADE, related_name="questiontheme"
    )
    text = models.TextField()
    answer = models.TextField()

    def __str__(self) -> str:
        return f"{self.theme}: {self.text}"

    class Meta:
        verbose_name = "область знания вопроса"
