from django import forms

from questions.models import Section


class CreateInterviewForm(forms.Form):
    sections = forms.ModelMultipleChoiceField(
        queryset=Section.objects.all().prefetch_related("theme"),
        widget=forms.CheckboxSelectMultiple,
    )
