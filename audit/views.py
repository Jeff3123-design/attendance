from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.mixins import RoleRequiredMixin
from .models import AuditLog


class AuditLogListView(LoginRequiredMixin, RoleRequiredMixin, TemplateView):
    allowed_roles = ['SUPER_ADMIN', 'SCHOOL_ADMIN']
    template_name = 'audit/logs.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['page_title'] = "System Security & Audit Trail"
        ctx['breadcrumb_title'] = "Audit Logs"
        ctx['logs'] = AuditLog.objects.select_related('user').all()[:50]
        return ctx
