from django import forms

from .models import Section


def build_create_interview_form():
    sections = {}
    for section in Section.objects.prefetch_related("theme").all():
        sections[str(section.name)] = forms.MultipleChoiceField(
            choices=(
                (theme.id, theme.name) for theme in section.theme.all()
            ),
            widget=forms.CheckboxSelectMultiple,
        )
    return type('CreateInterviewForm', (forms.Form, ), sections)