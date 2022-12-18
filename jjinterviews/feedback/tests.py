from django.test import TestCase
from django.urls import reverse

from feedback.forms import FeedBackForm
from feedback.models import FeedBack


class FormTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.form = FeedBackForm()

    def test_mail_label(self):
        name_label = self.form.fields["mail"].label
        self.assertEquals(name_label, "Почта")

    def test_mail_help_text(self):
        name_help_text = self.form.fields["mail"].help_text
        self.assertEquals(name_help_text, "Введите вашу почту.")

    def test_text_label(self):
        name_label = self.form.fields["text"].label
        self.assertEquals(name_label, "Содержимое")

    def test_text_help_text(self):
        name_help_text = self.form.fields["text"].help_text
        self.assertEquals(name_help_text,
                          "В этом поле введите текст своего обращения.")

    def test_create_task(self):
        feedbacks_count = FeedBack.objects.count()
        test_mail = "user@user.ru"
        form_data = {
            "mail": test_mail,
            "text": "text text",
        }
        response = self.client.post(
            reverse("feedback:main"),
            data=form_data,
            follow=True,
        )
        self.assertRedirects(response, reverse("feedback:main"))
        self.assertEqual(FeedBack.objects.count(), feedbacks_count + 1)
        self.assertTrue(
            FeedBack.objects.filter(
                mail=test_mail,
            ).exists()
        )

    def test_item_list_page_show_correct_context(self):
        response = self.client.get(reverse("feedback:main"))
        self.assertIn("form", response.context)
        self.assertEqual(len(list(response.context["form"])), 2)
