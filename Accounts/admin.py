from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Extra Info", {
            "fields": (
                "role",
                "gender",
                "phone_number",
                "date_of_birth",
                "profile_picture",
                "address",
                "city",
                "is_verified",
            )
        }),
    )

    list_display = ("email", "first_name", "last_name", "role", "is_staff")
    list_filter = ("role", "is_staff", "is_superuser")

@admin.register(InviteCode)
class InviteCodeAdmin(admin.ModelAdmin):
    list_display = ("code", "role", "is_used", "expires_at")
    search_fields = ("code",)
    list_filter = ("role", "is_used")
