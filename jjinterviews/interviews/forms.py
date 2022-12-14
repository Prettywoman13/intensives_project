from collections import defaultdict

from django import forms

from questions.models import Section


def build_create_interview_form():
    sections = {}
    for section in Section.objects.prefetch_related("theme").all():
        sections[str(section.id)] = forms.MultipleChoiceField(
            choices = (
                (theme.id, theme.name) for theme in section.theme.all()
            )
        )
    return type('CreateInterviewForm', (forms.Form, ), sections)
