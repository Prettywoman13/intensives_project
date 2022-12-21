from django import forms

from .models import Question, Theme


class NewQuestionForm(forms.Form):
    """
    Форма создания вопроса
    """
    theme = forms.ModelChoiceField(queryset=Theme.objects.all(),
                                   label="Тема вопроса")
    question = forms.CharField(max_length=200, label="Вопрос")
    answer = forms.CharField(widget=forms.Textarea, label="Ответ")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"

    def save(self):
        data = self.cleaned_data
        question = Question()
        question.theme = data["theme"]
        question.text = data["question"]
        question.answer = data["answer"]
        question.save()

    class Meta:
        help_texts = {
            "theme": "Тема вопроса.",
            "question": "Ваш вопрос.",
            "answer": "Ответ на вопрос."
        }
