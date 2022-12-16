from django import forms
from django.db.utils import OperationalError

from questions.models import Section


def build_create_interview_form(*args, **kwargs):
    sections = {
        "Почта": forms.EmailField(
            widget=forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Почта стажёра",
                    "id": "Username",
                    "type": "email",
                    "aria-describedby": "emailHelp",
                }
            )
        )
    }
    try:
        for section in Section.objects.prefetch_related("theme").all():
            if section.theme.count() > 0:
                sections[str(section.name)] = forms.MultipleChoiceField(
                    choices=(
                        (theme.id, theme.name)
                        for theme in section.theme.prefetch_related("question")
                        if theme.question.exists()
                    ),
                    widget=forms.CheckboxSelectMultiple(),
                    required=False,
                )
    except OperationalError:
        """
        Тк форма динамическая, она выполняется еще до загрузке базы,
        в которой может не быть таблицы
        (срабатывает один раз еще до наката миграций)
        """
        pass
    return type("CreateInterviewForm", (forms.Form,), sections)
