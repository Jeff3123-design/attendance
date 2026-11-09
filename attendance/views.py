from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.mixins import RoleRequiredMixin
from .models import AttendanceLog, DailyAttendance


class TodayAttendanceView(LoginRequiredMixin, RoleRequiredMixin, TemplateView):
    allowed_roles = ['SUPER_ADMIN', 'SCHOOL_ADMIN', 'TEACHER', 'BURSAR']
    template_name = 'attendance/today.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['page_title'] = "Today's Attendance Roll"
        ctx['breadcrumb_title'] = "Today"
        return ctx


class AttendanceLogsView(LoginRequiredMixin, RoleRequiredMixin, TemplateView):
    allowed_roles = ['SUPER_ADMIN', 'SCHOOL_ADMIN', 'TEACHER']
    template_name = 'attendance/logs.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['page_title'] = "Raw Biometric Punch Logs"
        ctx['breadcrumb_title'] = "Raw Logs"
        user = self.request.user
        if getattr(user, 'is_super_admin', False) or user.is_superuser:
            ctx['logs'] = AttendanceLog.objects.all()[:50]
        elif hasattr(user, 'school') and user.school:
            ctx['logs'] = AttendanceLog.objects.filter(school=user.school)[:50]
        else:
            ctx['logs'] = AttendanceLog.objects.none()
        return ctx


class DailyAttendanceView(LoginRequiredMixin, RoleRequiredMixin, TemplateView):
    allowed_roles = ['SUPER_ADMIN', 'SCHOOL_ADMIN', 'TEACHER', 'BURSAR']
    template_name = 'attendance/daily.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['page_title'] = "Daily Attendance Register"
        ctx['breadcrumb_title'] = "Daily Register"
        user = self.request.user
        if getattr(user, 'is_super_admin', False) or user.is_superuser:
            ctx['records'] = DailyAttendance.objects.all()[:50]
        elif hasattr(user, 'school') and user.school:
            ctx['records'] = DailyAttendance.objects.filter(school=user.school)[:50]
        else:
            ctx['records'] = DailyAttendance.objects.none()
        return ctx


class ByClassAttendanceView(LoginRequiredMixin, RoleRequiredMixin, TemplateView):
    allowed_roles = ['SUPER_ADMIN', 'SCHOOL_ADMIN', 'TEACHER', 'BURSAR']
    template_name = 'attendance/by_class.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['page_title'] = "Attendance Roll by Class & Stream"
        ctx['breadcrumb_title'] = "By Class"
        return ctx


class ByDormAttendanceView(LoginRequiredMixin, RoleRequiredMixin, TemplateView):
    allowed_roles = ['SUPER_ADMIN', 'SCHOOL_ADMIN', 'TEACHER']
    template_name = 'attendance/by_dorm.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['page_title'] = "Boarding Dormitory Night Roll Call"
        ctx['breadcrumb_title'] = "By Dorm"
        return ctx


class LateAttendanceView(LoginRequiredMixin, RoleRequiredMixin, TemplateView):
    allowed_roles = ['SUPER_ADMIN', 'SCHOOL_ADMIN', 'TEACHER', 'BURSAR']
    template_name = 'attendance/late.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['page_title'] = "Late Arrivals Tracking"
        ctx['breadcrumb_title'] = "Late Arrivals"
        return ctx


class AbsentAttendanceView(LoginRequiredMixin, RoleRequiredMixin, TemplateView):
    allowed_roles = ['SUPER_ADMIN', 'SCHOOL_ADMIN', 'TEACHER', 'BURSAR']
    template_name = 'attendance/absent.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['page_title'] = "Absenteeism & Truancy Roster"
        ctx['breadcrumb_title'] = "Absent Students"
        return ctx


class ManualEntryAttendanceView(LoginRequiredMixin, RoleRequiredMixin, TemplateView):
    allowed_roles = ['SUPER_ADMIN', 'SCHOOL_ADMIN', 'TEACHER']
    template_name = 'attendance/manual_entry.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['page_title'] = "Manual Attendance Override / Entry"
        ctx['breadcrumb_title'] = "Manual Entry"
        return ctx


class AttendanceRulesView(LoginRequiredMixin, RoleRequiredMixin, TemplateView):
    allowed_roles = ['SUPER_ADMIN', 'SCHOOL_ADMIN']
    template_name = 'attendance/rules.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['page_title'] = "School Bell Schedule & Cutoff Times"
        ctx['breadcrumb_title'] = "Attendance Rules"
        return ctx
