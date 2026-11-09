from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.mixins import RoleRequiredMixin
from students.models import Student


class ReportIndexView(LoginRequiredMixin, RoleRequiredMixin, TemplateView):
    allowed_roles = ['SUPER_ADMIN', 'SCHOOL_ADMIN', 'TEACHER', 'BURSAR']
    template_name = 'reports/index.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['page_title'] = "Attendance Reports & Analytics"
        ctx['breadcrumb_title'] = "Reports"
        return ctx


class ReportDailyView(LoginRequiredMixin, RoleRequiredMixin, TemplateView):
    allowed_roles = ['SUPER_ADMIN', 'SCHOOL_ADMIN', 'TEACHER', 'BURSAR']
    template_name = 'reports/daily.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['page_title'] = "Daily Attendance Summary Report"
        ctx['breadcrumb_title'] = "Daily Report"
        return ctx


class ReportWeeklyView(LoginRequiredMixin, RoleRequiredMixin, TemplateView):
    allowed_roles = ['SUPER_ADMIN', 'SCHOOL_ADMIN', 'TEACHER', 'BURSAR']
    template_name = 'reports/weekly.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['page_title'] = "Weekly Attendance Trends Report"
        ctx['breadcrumb_title'] = "Weekly Report"
        return ctx


class ReportTermlyView(LoginRequiredMixin, RoleRequiredMixin, TemplateView):
    allowed_roles = ['SUPER_ADMIN', 'SCHOOL_ADMIN', 'TEACHER', 'BURSAR']
    template_name = 'reports/termly.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['page_title'] = "Termly Attendance Cumulative Report"
        ctx['breadcrumb_title'] = "Termly Report"
        return ctx


class ReportStudentView(LoginRequiredMixin, RoleRequiredMixin, TemplateView):
    allowed_roles = ['SUPER_ADMIN', 'SCHOOL_ADMIN', 'TEACHER', 'BURSAR']
    template_name = 'reports/student.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        student = Student.objects.filter(pk=pk).first()
        ctx['student'] = student
        ctx['student_id'] = pk
        ctx['page_title'] = f"Individual Attendance Dossier: {student.full_name}" if student else f"Student #{pk} Report"
        ctx['breadcrumb_title'] = "Student Report"
        return ctx


class ReportClassView(LoginRequiredMixin, RoleRequiredMixin, TemplateView):
    allowed_roles = ['SUPER_ADMIN', 'SCHOOL_ADMIN', 'TEACHER', 'BURSAR']
    template_name = 'reports/class.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        ctx['class_id'] = pk
        ctx['page_title'] = f"Class Attendance Analytics (Group #{pk})"
        ctx['breadcrumb_title'] = "Class Report"
        return ctx


class ReportExportView(LoginRequiredMixin, RoleRequiredMixin, TemplateView):
    allowed_roles = ['SUPER_ADMIN', 'SCHOOL_ADMIN', 'BURSAR']
    template_name = 'reports/export.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['page_title'] = "Export Attendance Data (Excel / PDF / CSV)"
        ctx['breadcrumb_title'] = "Export Center"
        return ctx
