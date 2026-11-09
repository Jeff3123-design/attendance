from django.contrib import admin
from .models import AuditLog


@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ('action', 'user', 'object_repr', 'ip_address', 'created_at')
    list_filter = ('action', 'created_at')
    search_fields = ('action', 'object_repr', 'user__username', 'ip_address')
    ordering = ('-created_at',)
