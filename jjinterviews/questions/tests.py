from django.test import TestCase

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
