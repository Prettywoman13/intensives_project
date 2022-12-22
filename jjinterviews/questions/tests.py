from django.test import TestCase
from django.urls import reverse

from users.models import User

from .forms import NewQuestionForm
from .models import Question, Section, Theme


class ModelsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.section = Section.objects.create(name="Секция 1")
        cls.theme = Theme.objects.create(name="Тема 1", section=cls.section)

    def test_section_create(self):
        item_count = Section.objects.count()
        self.item = Section(name="Тестовая секция")
        self.item.full_clean()
        self.item.save()
        self.assertEqual(Section.objects.count(), item_count + 1)

    def test_theme_create(self):
        item_count = Theme.objects.count()
        self.item = Theme(name="Тестовая тема", section=self.section)
        self.item.full_clean()
        self.item.save()
        self.assertEqual(Theme.objects.count(), item_count + 1)

    def test_question_create(self):
        item_count = Question.objects.count()
        self.item = Question(
            theme=self.theme, text="Тестоый вопрос", answer="Тестовый ответ"
        )
        self.item.full_clean()
        self.item.save()
        self.assertEqual(Question.objects.count(), item_count + 1)

    def test_several_questions_create(self):
        item_count = Question.objects.count()
        self.item = Question(
            theme=self.theme, text="Тестоый вопрос 1", answer="Тестовый ответ"
        )
        self.item.full_clean()
        self.item.save()
        self.item = Question(
            theme=self.theme, text="Тестоый вопрос 2", answer="Тестовый ответ"
        )
        self.item.full_clean()
        self.item.save()

        self.assertEqual(Question.objects.count(), item_count + 2)

    def tearDown(self):
        Question.objects.all().delete()
        Theme.objects.all().delete()
        Section.objects.all().delete()
        super().tearDown()


class FormTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.form = NewQuestionForm()

    @classmethod
    def setUpTestData(cls) -> None:
        super().setUpTestData()
        cls.user = User.objects.create_user("user@ya.ru", "smarttest")

    def test_theme_label(self):
        name_label = self.form.fields["theme"].label
        self.assertEquals(name_label, "Тема вопроса")

    def test_theme_help_text(self):
        name_help_text = self.form.fields["theme"].help_text
        self.assertEquals(name_help_text, "Область вопроса.")

    def test_text_label(self):
        name_label = self.form.fields["text"].label
        self.assertEquals(name_label, "Вопрос")

    def test_text_help_text(self):
        name_help_text = self.form.fields["text"].help_text
        self.assertEquals(name_help_text, "Ваш вопрос.")

    def test_answer_label(self):
        name_label = self.form.fields["answer"].label
        self.assertEquals(name_label, "Ответ")

    def test_answer_help_text(self):
        name_help_text = self.form.fields["answer"].help_text
        self.assertEquals(name_help_text, "Ответ на вопрос.")

    def test_item_list_page_show_correct_context(self):
        self.assertTrue(self.client.login(username="user@ya.ru",
                                          password="smarttest"))
        response = self.client.get(reverse("questions:new"))
        self.assertIn("form", response.context)
        self.assertEqual(len(list(response.context["form"])), 3)

    def tearDown(self):
        User.objects.all().delete()
        super().tearDown()
