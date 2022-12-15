from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from users.forms import CustomUserChangeForm, CustomUserCreationForm
from users.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ("email", "is_active", "date_joined")
    list_filter = (
        "email",
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
                    "avatar",
                    "nickname",
                )
            },
        ),
        ("Permissions", {"fields": ("is_active", "is_staff")}),
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
                    "is_active",
                ),
            },
        ),
    )


admin.site.unregister(Group)
