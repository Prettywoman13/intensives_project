from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse

from questions.models import Question, Section, Theme
from users.models import User

from .models import Interview, Pack, QuestionStatistic


class ModelsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.user = User.objects.create(
            email="test@test.ru",
            password="password",
        )
        cls.section = Section.objects.create(name="секция")
        cls.theme = Theme.objects.create(name="тема", section=cls.section)
        cls.question1 = Question.objects.create(
            theme=cls.theme, text="вопрос1", answer="ответ1"
        )
        cls.question2 = Question.objects.create(
            theme=cls.theme, text="вопрос2", answer="ответ2"
        )
        cls.pack = Pack.objects.create()
        cls.pack.questions.add(cls.question1)
        cls.pack.questions.add(cls.question2)
        cls.interview = Interview.objects.create(
            email_interviewed="user1@user.ru",
            user=cls.user,
            pack=cls.pack,
        )

    def test_pack_create(self):
        item_count = Pack.objects.count()
        self.item = Pack()
        self.item.full_clean()
        self.item.save()
        self.item.questions.add(self.question1)
        self.item.questions.add(self.question2)
        self.item.full_clean()
        self.item.save()
        self.assertEqual(Pack.objects.count(), item_count + 1)

    def test_interview_create_without_email(self):
        item_count = Interview.objects.count()
        self.item = Interview(user=self.user, pack=self.pack)
        with self.assertRaises(ValidationError):
            self.item.full_clean()
            self.item.save()
        self.assertEqual(Interview.objects.count(), item_count)

    def test_interview_create(self):
        item_count = Interview.objects.count()
        self.item = Interview(
            email_interviewed="user@user.ru",
            user=self.user,
            pack=self.pack,
        )
        self.item.full_clean()
        self.item.save()
        self.assertEqual(Interview.objects.count(), item_count + 1)

    def test_questionstatistic_create_without_email(self):
        item_count = QuestionStatistic.objects.count()
        self.item = QuestionStatistic(
            question=self.question1,
            user=self.user,
            interview=self.interview,
            mark=True,
        )
        with self.assertRaises(ValidationError):
            self.item.full_clean()
            self.item.save()
        self.assertEqual(QuestionStatistic.objects.count(), item_count)

    def test_questionstatistic_create(self):
        item_count = QuestionStatistic.objects.count()
        self.item = QuestionStatistic(
            email_interviewed="user@user.ru",
            question=self.question1,
            user=self.user,
            interview=self.interview,
            mark=True,
        )
        self.item.full_clean()
        self.item.save()
        self.assertEqual(QuestionStatistic.objects.count(), item_count + 1)

    def tearDown(self):
        QuestionStatistic.objects.all().delete()
        Interview.objects.all().delete()
        Pack.objects.all().delete()
        super().tearDown()


class TaskPagesTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.user = User.objects.create(
            email="test@test.ru",
            password="password",
        )
        cls.section = Section.objects.create(name="секция")
        cls.theme = Theme.objects.create(name="тема", section=cls.section)
        cls.question1 = Question.objects.create(
            theme=cls.theme, text="вопрос1", answer="ответ1"
        )
        cls.question2 = Question.objects.create(
            theme=cls.theme, text="вопрос2", answer="ответ2"
        )
        cls.pack = Pack.objects.create()
        cls.pack.questions.add(cls.question1)
        cls.pack.questions.add(cls.question2)

    def test_interview_page_show_correct_content(self):
        self.item = Interview.objects.create(
            email_interviewed="user1@user.ru", user=self.user, pack=self.pack
        )
        self.item.full_clean()
        self.item.save()
        self.client.force_login(self.user)
        response = self.client.get(
            reverse(
                "interview:interview", kwargs={"interview_id": self.item.id}
            )
        )

        self.assertIn("page_obj", response.context)
        self.assertEqual(len(response.context["page_obj"]), 1)

    def tearDown(self):
        QuestionStatistic.objects.all().delete()
        Interview.objects.all().delete()
        Pack.objects.all().delete()
        super().tearDown()
