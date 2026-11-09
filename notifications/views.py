from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.mixins import RoleRequiredMixin
from .models import SmsLog


class SmsLogListView(LoginRequiredMixin, RoleRequiredMixin, TemplateView):
    allowed_roles = ['SUPER_ADMIN', 'SCHOOL_ADMIN', 'BURSAR']
    template_name = 'notifications/sms_logs.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['page_title'] = "Parent SMS Broadcast Log"
        ctx['breadcrumb_title'] = "SMS Logs"
        user = self.request.user
        if getattr(user, 'is_super_admin', False) or user.is_superuser:
            ctx['logs'] = SmsLog.objects.all()[:50]
        elif hasattr(user, 'school') and user.school:
            ctx['logs'] = SmsLog.objects.filter(school=user.school)[:50]
        else:
            ctx['logs'] = SmsLog.objects.none()
        return ctx


class SmsTemplatesView(LoginRequiredMixin, RoleRequiredMixin, TemplateView):
    allowed_roles = ['SUPER_ADMIN', 'SCHOOL_ADMIN']
    template_name = 'notifications/templates.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['page_title'] = "Automated SMS Templates"
        ctx['breadcrumb_title'] = "SMS Templates"
        return ctx


class SmsSettingsView(LoginRequiredMixin, RoleRequiredMixin, TemplateView):
    allowed_roles = ['SUPER_ADMIN', 'SCHOOL_ADMIN']
    template_name = 'notifications/settings.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['page_title'] = "SMS Gateway Provider Configuration"
        ctx['breadcrumb_title'] = "SMS Settings"
        return ctx


class SmsSendView(LoginRequiredMixin, RoleRequiredMixin, TemplateView):
    allowed_roles = ['SUPER_ADMIN', 'SCHOOL_ADMIN', 'TEACHER']
    template_name = 'notifications/send.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['page_title'] = "Send Custom SMS Broadcast to Parents"
        ctx['breadcrumb_title'] = "Send SMS"
        return ctx
