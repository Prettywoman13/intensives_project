# from django import forms
# from django.contrib import admin

# from .models import Theme, Question, Section


# class PersonAdminForm(forms.ModelForm):
#     themes = forms.ChoiceField(choices=[])

#     def __init__(self, *args, **kwargs) -> None:
#         super().__init__(*args, **kwargs)
#         self.fields["themes"] = forms.ChoiceField(
#             label="Выбрать тему",
#             choices=[["Не указано", "Не указано"]]
#             + [
#                 [item.id, f"{item.type}: {item.text}"]
#                 for item in Item.objects.exclude(type="Вопрос")
#             ],
#         )

#     class Meta:
#         model = Item
#         fields = "__all__"

# @admin.register(Section)
# class Section(admin.ModelAdmin):
#     ...


# @admin.register(Theme)
# class Theme(admin.ModelAdmin):
#     ...


# @admin.register(Question)
# class QuestionAdmin(admin.ModelAdmin):
    # ...
    # form = PersonAdminForm
    # list_display = ("type", "text", "path")
    # fieldsets = (
    #     (
    #         None,
    #         {"fields": ("type", "text", "path")},
    #     ),
    #     ("Категория | Область знаний", {"fields": ("themes",)}),
    # )
    # list_filter = ("type",)
    # search_fields = ("text",)
    # ordering = ("type",)