from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.mixins import RoleRequiredMixin, SchoolScopedMixin
from .models import Student


class StudentListView(LoginRequiredMixin, RoleRequiredMixin, TemplateView):
    allowed_roles = ['SUPER_ADMIN', 'SCHOOL_ADMIN', 'TEACHER', 'BURSAR']
    template_name = 'students/list.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['page_title'] = 'Students Directory'
        ctx['breadcrumb_title'] = 'Students'
        user = self.request.user
        if getattr(user, 'is_super_admin', False) or user.is_superuser:
            ctx['students'] = Student.objects.all()[:50]
        elif hasattr(user, 'school') and user.school:
            ctx['students'] = Student.objects.filter(school=user.school)[:50]
        else:
            ctx['students'] = Student.objects.none()
        return ctx


class StudentCreateView(LoginRequiredMixin, RoleRequiredMixin, TemplateView):
    allowed_roles = ['SUPER_ADMIN', 'SCHOOL_ADMIN', 'TEACHER']
    template_name = 'students/form.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['page_title'] = 'Enroll New Student'
        ctx['breadcrumb_title'] = 'Add Student'
        ctx['action'] = 'Enroll'
        return ctx


class StudentDetailView(LoginRequiredMixin, RoleRequiredMixin, TemplateView):
    allowed_roles = ['SUPER_ADMIN', 'SCHOOL_ADMIN', 'TEACHER', 'BURSAR']
    template_name = 'students/detail.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        student = Student.objects.filter(pk=pk).first()
        ctx['student'] = student
        ctx['student_id'] = pk
        ctx['page_title'] = f"Student Profile: {student.full_name}" if student else f"Student #{pk}"
        ctx['breadcrumb_title'] = 'Student Profile'
        return ctx


class StudentUpdateView(LoginRequiredMixin, RoleRequiredMixin, TemplateView):
    allowed_roles = ['SUPER_ADMIN', 'SCHOOL_ADMIN', 'TEACHER']
    template_name = 'students/form.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        student = Student.objects.filter(pk=pk).first()
        ctx['student'] = student
        ctx['student_id'] = pk
        ctx['page_title'] = f"Edit Student: {student.full_name}" if student else f"Edit Student #{pk}"
        ctx['breadcrumb_title'] = 'Edit Student'
        ctx['action'] = 'Update'
        return ctx


class StudentImportView(LoginRequiredMixin, RoleRequiredMixin, TemplateView):
    allowed_roles = ['SUPER_ADMIN', 'SCHOOL_ADMIN']
    template_name = 'students/import.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['page_title'] = 'Bulk Student Import'
        ctx['breadcrumb_title'] = 'Import'
        return ctx


class StudentClassesView(LoginRequiredMixin, RoleRequiredMixin, TemplateView):
    allowed_roles = ['SUPER_ADMIN', 'SCHOOL_ADMIN', 'TEACHER', 'BURSAR']
    template_name = 'students/classes.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['page_title'] = 'Classes & Streams Directory'
        ctx['breadcrumb_title'] = 'Classes'
        return ctx


class StudentDormsView(LoginRequiredMixin, RoleRequiredMixin, TemplateView):
    allowed_roles = ['SUPER_ADMIN', 'SCHOOL_ADMIN', 'TEACHER']
    template_name = 'students/dorms.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['page_title'] = 'Dormitories & Hostels'
        ctx['breadcrumb_title'] = 'Dormitories'
        return ctx
