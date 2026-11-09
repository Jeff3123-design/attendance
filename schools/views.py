from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.mixins import RoleRequiredMixin
from .models import School


class SchoolListView(LoginRequiredMixin, RoleRequiredMixin, TemplateView):
    allowed_roles = ['SUPER_ADMIN']
    template_name = 'schools/list.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['page_title'] = 'Schools Directory'
        ctx['breadcrumb_title'] = 'Schools'
        ctx['schools'] = School.objects.all()
        return ctx


class SchoolCreateView(LoginRequiredMixin, RoleRequiredMixin, TemplateView):
    allowed_roles = ['SUPER_ADMIN']
    template_name = 'schools/form.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['page_title'] = 'Register New School'
        ctx['breadcrumb_title'] = 'Add School'
        ctx['action'] = 'Create'
        return ctx


class SchoolDetailView(LoginRequiredMixin, RoleRequiredMixin, TemplateView):
    allowed_roles = ['SUPER_ADMIN']
    template_name = 'schools/detail.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        school = School.objects.filter(pk=pk).first()
        ctx['school'] = school
        ctx['school_id'] = pk
        ctx['page_title'] = f"School: {school.name}" if school else f"School #{pk}"
        ctx['breadcrumb_title'] = 'School Detail'
        return ctx


class SchoolUpdateView(LoginRequiredMixin, RoleRequiredMixin, TemplateView):
    allowed_roles = ['SUPER_ADMIN']
    template_name = 'schools/form.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        school = School.objects.filter(pk=pk).first()
        ctx['school'] = school
        ctx['school_id'] = pk
        ctx['page_title'] = f"Edit School: {school.name}" if school else f"Edit School #{pk}"
        ctx['breadcrumb_title'] = 'Edit School'
        ctx['action'] = 'Update'
        return ctx
