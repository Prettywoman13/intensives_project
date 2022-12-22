from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(
        self, email, password, **extra_fields
    ) -> "user":  # noqa 821
        """
        Создает и сохраняет пользователя с указанным
        адресом электронной почты и паролем.
        """
        if not email:
            raise ValueError("Адрес электронной почты должен быть установлен")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        """
        Создание обычного пользователя, без прав админинстратора
        """
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        """
        Создание админ-пользователя
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Суперпользователь должен иметь is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(
                "Суперпользователь должен" "иметь is_superuser=True."
            )

        return self._create_user(email, password, **extra_fields)
