from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import RoleRequiredMixin


class ProfileSettingsView(LoginRequiredMixin, TemplateView):
    template_name = 'settings/profile.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['page_title'] = 'User Profile Settings'
        ctx['breadcrumb_title'] = 'Profile'
        return ctx


class SchoolSettingsView(LoginRequiredMixin, RoleRequiredMixin, TemplateView):
    allowed_roles = ['SUPER_ADMIN', 'SCHOOL_ADMIN']
    template_name = 'settings/school.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['page_title'] = 'School Configuration Settings'
        ctx['breadcrumb_title'] = 'School Settings'
        return ctx


class UserManagementView(LoginRequiredMixin, RoleRequiredMixin, TemplateView):
    allowed_roles = ['SUPER_ADMIN', 'SCHOOL_ADMIN']
    template_name = 'settings/users.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['page_title'] = 'User Management'
        ctx['breadcrumb_title'] = 'Users'
        return ctx


class UserAddView(LoginRequiredMixin, RoleRequiredMixin, TemplateView):
    allowed_roles = ['SUPER_ADMIN', 'SCHOOL_ADMIN']
    template_name = 'settings/users_add.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['page_title'] = 'Create New User'
        ctx['breadcrumb_title'] = 'Add User'
        return ctx


class ConsentPolicySettingsView(LoginRequiredMixin, RoleRequiredMixin, TemplateView):
    allowed_roles = ['SUPER_ADMIN', 'SCHOOL_ADMIN']
    template_name = 'settings/consent.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['page_title'] = 'Biometric Consent & Data Protection Policy'
        ctx['breadcrumb_title'] = 'Consent Policy'
        return ctx


class BackupSettingsView(LoginRequiredMixin, RoleRequiredMixin, TemplateView):
    allowed_roles = ['SUPER_ADMIN']
    template_name = 'settings/backup.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['page_title'] = 'Database & System Backup'
        ctx['breadcrumb_title'] = 'Backups'
        return ctx
