from django import forms

from questions.models import Section


def build_create_interview_form():
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
    for section in Section.objects.prefetch_related("theme").all():
        sections[str(section.name)] = forms.MultipleChoiceField(
            choices=((theme.id, theme.name) for theme in section.theme.all()),
            widget=forms.CheckboxSelectMultiple(
                attrs={
                    "class": "form-check-input",
                    "type": "checkbox",
                    "id": "flexCheckIndeterminate",
                }
            ),
            required=False,
        )
    return type("CreateInterviewForm", (forms.Form,), sections)
