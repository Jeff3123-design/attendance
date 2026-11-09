from django.contrib import admin
from .models import AttendanceLog, DailyAttendance


@admin.register(AttendanceLog)
class AttendanceLogAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'timestamp', 'punch_type', 'device', 'school', 'created_at')
    list_filter = ('school', 'device', 'punch_type', 'timestamp')
    search_fields = ('user_id', 'device__name', 'device__serial_number')
    ordering = ('-timestamp',)


@admin.register(DailyAttendance)
class DailyAttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'date', 'status', 'first_in', 'last_out', 'school')
    list_filter = ('school', 'status', 'date')
    search_fields = ('student__full_name', 'student__admission_number')
    ordering = ('-date', 'student')
