from django import forms

from .models import Question, Theme


class NewQuestionForm(forms.ModelForm):
    """
    Форма создания вопроса
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"

    theme = forms.ModelChoiceField(
        queryset=Theme.objects.all(), label="Тема вопроса",
        help_text="Область вопроса."
    )

    class Meta:
        model = Question
        fields = "__all__"
        help_texts = {
            "text": "Ваш вопрос.",
            "answer": "Ответ на вопрос.",
        }
