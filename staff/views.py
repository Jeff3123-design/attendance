from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.mixins import RoleRequiredMixin
from .models import Staff


class StaffListView(LoginRequiredMixin, RoleRequiredMixin, TemplateView):
    allowed_roles = ['SUPER_ADMIN', 'SCHOOL_ADMIN', 'TEACHER', 'BURSAR']
    template_name = 'staff/list.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['page_title'] = 'Staff Directory'
        ctx['breadcrumb_title'] = 'Staff'
        user = self.request.user
        if getattr(user, 'is_super_admin', False) or user.is_superuser:
            ctx['staff_list'] = Staff.objects.all()[:50]
        elif hasattr(user, 'school') and user.school:
            ctx['staff_list'] = Staff.objects.filter(school=user.school)[:50]
        else:
            ctx['staff_list'] = Staff.objects.none()
        return ctx


class StaffCreateView(LoginRequiredMixin, RoleRequiredMixin, TemplateView):
    allowed_roles = ['SUPER_ADMIN', 'SCHOOL_ADMIN']
    template_name = 'staff/form.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['page_title'] = 'Add New Staff Member'
        ctx['breadcrumb_title'] = 'Add Staff'
        ctx['action'] = 'Create'
        return ctx


class StaffDetailView(LoginRequiredMixin, RoleRequiredMixin, TemplateView):
    allowed_roles = ['SUPER_ADMIN', 'SCHOOL_ADMIN', 'TEACHER', 'BURSAR']
    template_name = 'staff/detail.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        member = Staff.objects.filter(pk=pk).first()
        ctx['member'] = member
        ctx['staff_id'] = pk
        ctx['page_title'] = f"Staff Profile: {member.full_name}" if member else f"Staff Member #{pk}"
        ctx['breadcrumb_title'] = 'Staff Profile'
        return ctx


class StaffUpdateView(LoginRequiredMixin, RoleRequiredMixin, TemplateView):
    allowed_roles = ['SUPER_ADMIN', 'SCHOOL_ADMIN']
    template_name = 'staff/form.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        member = Staff.objects.filter(pk=pk).first()
        ctx['member'] = member
        ctx['staff_id'] = pk
        ctx['page_title'] = f"Edit Staff: {member.full_name}" if member else f"Edit Staff #{pk}"
        ctx['breadcrumb_title'] = 'Edit Staff'
        ctx['action'] = 'Update'
        return ctx
