from django.contrib import admin
from .models import Device


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'serial_number', 'school', 'location', 'ip_address', 'last_seen', 'is_active')
    list_filter = ('school', 'location', 'is_active')
    search_fields = ('name', 'serial_number', 'ip_address')
    ordering = ('school', 'name')
