from django import forms

from .models import Question, Theme, Section


class NewQuestionForm(forms.ModelForm):
    """
    Форма создания вопроса
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"

    theme = forms.ModelChoiceField(
        queryset=Theme.objects.all(), label="Тема вопроса"
    )
    text = forms.CharField(max_length=200, label="Вопрос")
    answer = forms.CharField(widget=forms.Textarea, label="Ответ")

    class Meta:
        model = Question
        fields = "__all__"
        help_texts = {
            "theme": "Область вопроса.",
            "text": "Ваш вопрос.",
            "answer": "Ответ на вопрос.",
        }


def build_create_interview_form(*args, **kwargs) -> forms.Form:
    """
    Функция, строящая динамическую форму для генерации собеса
    """
    sections = {
        "Вопроc": forms.EmailField(
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
    sections["Вопросы"] = forms.ChoiceField(choices=(
        ((section.name, f'{section.name}:{section.theme.all()}')) for section in Section.objects.all().prefetch_related("theme") if section.theme.exists()
    ))
    # for section in Section.objects.prefetch_related("theme").all():
    #     if section.theme.count() > 0:
    #         sections["Вопросы"] = forms.ChoiceField(
    #             choices=(
    #                 (section.name, f'{section.name}: {theme.name}')
    #                 for theme in section.theme
    #                 if theme.question.exists()
    #             ),

    #             required=False,
    #         )
    return type("CreateInterviewForm", (forms.Form,), sections)
