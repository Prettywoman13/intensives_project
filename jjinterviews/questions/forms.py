from django import forms

from django_summernote.widgets import SummernoteWidget

from .models import Theme


def build_add_question_form(*args, **kwargs) -> forms.Form:
    """
    Функция, строящая динамическую форму для добавления вопросов
    """
    sections = {
        "Вопрос": forms.CharField(),
        "Ответ": forms.CharField(widget=SummernoteWidget()),
    }
    sections["Тема вопроса"] = forms.ChoiceField(
        choices=(
            (
                (theme.pk, f"{theme.section.name}:{theme.name}")
                for theme in Theme.objects.all().prefetch_related("section")
            )
        ),
    )
    return type("CreateInterviewForm", (forms.Form,), sections)
