from django.contrib import admin
from .models import SmsLog


@admin.register(SmsLog)
class SmsLogAdmin(admin.ModelAdmin):
    list_display = ('recipient', 'status', 'school', 'created_at')
    list_filter = ('school', 'status', 'created_at')
    search_fields = ('recipient', 'message')
    ordering = ('-created_at',)
