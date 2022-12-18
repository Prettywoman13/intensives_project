from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin

from .models import Question, Section, Theme


@admin.register(Section)
class Section(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Theme)
class Theme(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Question)
class QuestionThemeAdmin(SummernoteModelAdmin):
    list_display = ("id", "text")
    summernote_fields = ("answer",)
