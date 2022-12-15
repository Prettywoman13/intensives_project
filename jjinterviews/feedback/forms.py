from django import forms
from feedback.models import FeedBack


class FeedBackForm(forms.ModelForm):
    """
    Форма обратной связи
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = FeedBack
        fields = ("text", "mail")
        help_texts = {
            "text": "В этом поле введите текст своего обращения.",
            "mail": "Введите вашу почту.",
        }
