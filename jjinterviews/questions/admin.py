from django.contrib import admin

from .models import QuestionTheme, Section, Theme


@admin.register(Section)
class Section(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Theme)
class Theme(admin.ModelAdmin):
    list_display = ("id", "name")

    # Тестил тут)
    # def __init__(self, *args, **kwargs) -> None:
    #     super().__init__(*args, **kwargs)
    #     result = []
    #     for el in [5, 2, 4]:
    #         timer = []
    #         for theme in QuestionTheme.objects.filter(theme=el):
    #             print(theme)
    #             timer.append(theme.text)
    #         result += [timer]
    #     print(result)


@admin.register(QuestionTheme)
class QuestionThemeAdmin(admin.ModelAdmin):
    list_display = ("id", "text")
