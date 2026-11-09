from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.mixins import RoleRequiredMixin
from .models import Device


class DeviceListView(LoginRequiredMixin, RoleRequiredMixin, TemplateView):
    allowed_roles = ['SUPER_ADMIN', 'SCHOOL_ADMIN', 'TEACHER']
    template_name = 'devices/list.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['page_title'] = 'Biometric Fingerprint Terminals'
        ctx['breadcrumb_title'] = 'Devices'
        user = self.request.user
        if getattr(user, 'is_super_admin', False) or user.is_superuser:
            ctx['devices'] = Device.objects.all()
        elif hasattr(user, 'school') and user.school:
            ctx['devices'] = Device.objects.filter(school=user.school)
        else:
            ctx['devices'] = Device.objects.none()
        return ctx


class DeviceCreateView(LoginRequiredMixin, RoleRequiredMixin, TemplateView):
    allowed_roles = ['SUPER_ADMIN', 'SCHOOL_ADMIN']
    template_name = 'devices/form.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['page_title'] = 'Register New Terminal'
        ctx['breadcrumb_title'] = 'Add Device'
        ctx['action'] = 'Register'
        return ctx


class DeviceDetailView(LoginRequiredMixin, RoleRequiredMixin, TemplateView):
    allowed_roles = ['SUPER_ADMIN', 'SCHOOL_ADMIN', 'TEACHER']
    template_name = 'devices/detail.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        device = Device.objects.filter(pk=pk).first()
        ctx['device'] = device
        ctx['device_id'] = pk
        ctx['page_title'] = f"Device: {device.name}" if device else f"Device #{pk}"
        ctx['breadcrumb_title'] = 'Device Detail'
        return ctx


class DeviceUpdateView(LoginRequiredMixin, RoleRequiredMixin, TemplateView):
    allowed_roles = ['SUPER_ADMIN', 'SCHOOL_ADMIN']
    template_name = 'devices/form.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        device = Device.objects.filter(pk=pk).first()
        ctx['device'] = device
        ctx['device_id'] = pk
        ctx['page_title'] = f"Edit Device: {device.name}" if device else f"Edit Device #{pk}"
        ctx['breadcrumb_title'] = 'Edit Device'
        ctx['action'] = 'Update'
        return ctx


class DeviceEnrollView(LoginRequiredMixin, RoleRequiredMixin, TemplateView):
    allowed_roles = ['SUPER_ADMIN', 'SCHOOL_ADMIN', 'TEACHER']
    template_name = 'devices/enroll.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        device = Device.objects.filter(pk=pk).first()
        ctx['device'] = device
        ctx['device_id'] = pk
        ctx['page_title'] = f"Fingerprint Enrolment Guide ({device.name if device else f'Device #{pk}'})"
        ctx['breadcrumb_title'] = 'Biometric Enrolment'
        return ctx


class DeviceSyncStatusView(LoginRequiredMixin, RoleRequiredMixin, TemplateView):
    allowed_roles = ['SUPER_ADMIN', 'SCHOOL_ADMIN', 'TEACHER']
    template_name = 'devices/sync_status.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['page_title'] = 'ZKTeco ADMS / Cloud PUSH Sync Monitor'
        ctx['breadcrumb_title'] = 'Sync Status'
        return ctx
