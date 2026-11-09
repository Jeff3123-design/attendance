from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('admission_number', 'full_name', 'school', 'class_name', 'stream', 'gender', 'guardian_phone', 'consent_given', 'is_active')
    list_filter = ('school', 'class_name', 'stream', 'gender', 'consent_given', 'is_active')
    search_fields = ('admission_number', 'full_name', 'guardian_name', 'guardian_phone', 'dorm')
    ordering = ('school', 'admission_number')
