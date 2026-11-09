from django.contrib import admin
from .models import School


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'county', 'phone', 'email', 'is_active', 'created_at')
    list_filter = ('county', 'is_active')
    search_fields = ('name', 'code', 'county', 'email', 'phone')
    ordering = ('name',)
