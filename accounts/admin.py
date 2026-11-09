from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'role', 'school', 'is_staff', 'is_active')
    list_filter = ('role', 'school', 'is_staff', 'is_active')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)

    fieldsets = UserAdmin.fieldsets + (
        ('Biometric Attendance & Tenancy', {
            'fields': ('role', 'school')
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Biometric Attendance & Tenancy', {
            'fields': ('role', 'school')
        }),
    )
