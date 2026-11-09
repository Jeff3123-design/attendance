from django.contrib import admin
from .models import Staff


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('staff_number', 'full_name', 'school', 'department', 'phone', 'is_active')
    list_filter = ('school', 'department', 'is_active')
    search_fields = ('staff_number', 'full_name', 'department', 'phone')
    ordering = ('school', 'staff_number')
