import os
from pathlib import Path

import environ
from django_cleanup.signals import cleanup_pre_delete
from sorl.thumbnail import delete

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))


def is_env_true(env_name):
    return env(env_name, default="False").lower() == "true"


SECRET_KEY = env("SECRET_KEY")

DEBUG = is_env_true("DEBUG")

if DEBUG:
    ALLOWED_HOSTS = ["*"]
else:
    hosts_string = env("ALLOWED_HOSTS")
    if hosts_string:
        ALLOWED_HOSTS = hosts_string.split(",")

INTERNAL_IPS = [
    "127.0.0.1",
]

IMPORT_EXPORT_USE_TRANSACTIONS = True

INSTALLED_APPS = [
    "users.apps.UsersConfig",
    "questions.apps.QuestionsConfig",
    "interviews.apps.InterviewsConfig",
    "homepage.apps.HomepageConfig",
    "feedback.apps.FeedbackConfig",
    "core.apps.CoreConfig",
    "statistic.apps.StatisticConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "debug_toolbar",
    "django_summernote",
    "sorl.thumbnail",
    "django_cleanup.apps.CleanupConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = "jjinterviews.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

STATIC_URL = os.path.join(BASE_DIR, "/static/")

STATICFILES_DIRS = (os.path.join(BASE_DIR, "static_dev"),)

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = "send_mails/"

WSGI_APPLICATION = "jjinterviews.wsgi.application"

USE_SQLITE = is_env_true("USE_SQLITE")

SQLITE_SETTINGS = {
    "ENGINE": "django.db.backends.sqlite3",
    "NAME": BASE_DIR / "db.sqlite3",
}

POSTGRESQL_SETTINGS = {
    "ENGINE": "django.db.backends.postgresql",
    "NAME": env("DB_NAME", default="postgres"),
    "USER": env("DB_USER", default="postgres"),
    "PASSWORD": env("DB_PASSWORD", default="postgres"),
    "HOST": env("HOST", default="127.0.0.1"),
    "PORT": env("PORT", default="5432"),
}

DATABASES = {
    "default": SQLITE_SETTINGS if USE_SQLITE else POSTGRESQL_SETTINGS,
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation."
        "UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation."
        "MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation."
        "CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation."
        "NumericPasswordValidator",
    },
]

AUTH_USER_MODEL = "users.User"
AUTH_PROFILE_MODEL = "users.User"

LANGUAGE_CODE = "ru-RU"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGIN_URL = "/auth/login/"
LOGIN_REDIRECT_URL = "/"


def sorl_delete(**kwargs):
    print(kwargs)
    delete(kwargs["file"])


cleanup_pre_delete.connect(sorl_delete)

SUMMERNOTE_THEME = "bs4"

SUMMERNOTE_CONFIG = {
    "iframe": True,
    "summernote": {
        "airMode": False,
        "width": "100%",
        "height": "480",
        "toolbar": [
            ["style", ["style"]],
            ["font", ["bold", "underline", "clear"]],
            ["fontname", ["fontname"]],
            ["color", ["color"]],
            ["para", ["ul", "ol", "paragraph"]],
            ["table", ["table"]],
            ["insert", ["link"]],
            ["view", ["fullscreen", "codeview", "help"]],
        ],
    },
}
