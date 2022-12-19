from django.test import Client, TestCase
from django.core.exceptions import ValidationError
from django.urls import reverse

from .forms import (CustomUserCreationForm, CustomUserChangeForm,
                    UserLoginForm, UserUpdateForm,
                    CustomPasswordResetForm, CustomPasswordResetConfirmForm)
from .models import User


class ModelsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()

    def test_user_create_with_nothing(self):
        item_count = User.objects.count()
        self.item = User()
        with self.assertRaises(ValidationError):
            self.item.full_clean()
            self.item.save()
        self.assertEqual(User.objects.count(), item_count)

    def test_user_create_with_email_only(self):
        item_count = User.objects.count()
        self.item = User(email="user@user.ru")
        with self.assertRaises(ValidationError):
            self.item.full_clean()
            self.item.save()
        self.assertEqual(User.objects.count(), item_count)

    def test_user_create_with_nickname(self):
        item_count = User.objects.count()
        self.item = User(email="user@user.ru",
                         password="password",
                         nickname="nick")
        self.item.full_clean()
        self.item.save()
        self.assertEqual(User.objects.count(), item_count + 1)

    def test_user_create(self):
        item_count = User.objects.count()
        self.item = User(email="user@user.ru", password="password")
        self.item.full_clean()
        self.item.save()
        self.assertEqual(User.objects.count(), item_count + 1)

    def tearDown(self):
        User.objects.all().delete()
        super().tearDown()


class FormTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User(email="user@user.ru", password="password")
        cls.form = CustomUserCreationForm()
        cls.custom_user = CustomUserChangeForm()
        cls.login_form = UserLoginForm()
        cls.update_form = UserUpdateForm()
        cls.reset_form = CustomPasswordResetForm()
        cls.reset_confirm_form = CustomPasswordResetConfirmForm(user=cls.user)

    def test_name_password1_label(self):
        name_label = self.form.fields["password1"].label
        self.assertEquals(name_label, "Пароль")

    def test_name_password2_label(self):
        name_label = self.form.fields["password2"].label
        self.assertEquals(name_label, "Повторите пароль")

    def test_name_email_label(self):
        name_label = self.form.fields["email"].label
        self.assertEquals(name_label, "Почта")

    def test_name_email_label_custom_user(self):
        name_label = self.custom_user.fields["email"].label
        self.assertEquals(name_label, "Почта")

    def test_name_username_label_login_form(self):
        name_label = self.login_form.fields["username"].label
        self.assertEquals(name_label, "Почта")

    def test_name_password_label_login_form(self):
        name_label = self.login_form.fields["password"].label
        self.assertEquals(name_label, "Пароль")

    def test_name_email_label_update_form(self):
        name_label = self.update_form.fields["email"].label
        self.assertEquals(name_label, "Почта")

    def test_name_avatar_label_update_form(self):
        name_label = self.update_form.fields["avatar"].label
        self.assertEquals(name_label, "Аватар")

    def test_name_nickname_label_update_form(self):
        name_label = self.update_form.fields["nickname"].label
        self.assertEquals(name_label, "Имя")

    def test_name_email_label_reset_form(self):
        name_label = self.reset_form.fields["email"].label
        self.assertEquals(name_label, "Адрес электронной почты")

    def test_name_password1_label_reset_confirm_form(self):
        name_label = self.reset_confirm_form.fields["new_password1"].label
        self.assertEquals(name_label, "Новый пароль")

    def test_name_password2_label_reset_confirm_form(self):
        name_label = self.reset_confirm_form.fields["new_password2"].label
        self.assertEquals(name_label, "Подтверждение нового пароля")

    def tearDown(self):
        User.objects.all().delete()
        super().tearDown()


class TaskPagesTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def test_profile_page_show_correct_content(self):
        self.item = User(email="user@user.ru", password="password")
        self.item.full_clean()
        self.item.save()

        response = Client().get(reverse("users:profile",
                                        kwargs={"pk": self.item.pk}))
        self.assertIsNone(response.context)

    def test_register_page_show_correct_content(self):
        response = Client().get(reverse("users:register"))
        self.assertIn("form", response.context)
        self.assertIn("view", response.context)

    def tearDown(self):
        User.objects.all().delete()
        super().tearDown()
