from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import (
    User,
    OwnerProfile,
    EmployeeProfile
)


class UserAdminConfig(UserAdmin):
    model = User
    search_fields = ("username",)
    list_filter = (
        "username",
        "email",
        "is_active",
        "user_type",
    )
    ordering = ("id",)
    list_display = ("__str__", "email", "user_type", "is_active",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "username",
                    "email",
                    "password",
                    "user_type"
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
    )

    # fieldsets to add a new user
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "password1",
                    "password2",
                    "user_type",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
    )

admin.site.register(User, UserAdminConfig)
admin.site.register(OwnerProfile)
admin.site.register(EmployeeProfile)