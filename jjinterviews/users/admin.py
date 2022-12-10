from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from users.forms import CustomUserChangeForm, CustomUserCreationForm
from users.models import Intern, User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ("email", "is_staff", "is_active", "date_joined")
    list_filter = (
        "email",
        "is_staff",
        "is_active",
    )
    search_fields = ("email",)
    ordering = ("email",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "password",
                    "first_name",
                    "last_name",
                    "birthday",
                )
            },
        ),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )


@admin.register(Intern)
class InternAdmin(admin.ModelAdmin):
    model = Intern
    list_display = ("interviewier", "email", "date_joined")
    list_filter = ("email", "date_joined")
    search_fields = ("email",)
    ordering = ("email",)


admin.site.unregister(Group)
