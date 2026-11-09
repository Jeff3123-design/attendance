from django.db import models
from django.conf import settings


class AuditLog(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='audit_logs',
        help_text="User who initiated the action"
    )
    action = models.CharField(max_length=255, help_text="Action performed e.g. LOGIN, CREATE_STUDENT, SYNC_TERMINAL")
    object_repr = models.CharField(max_length=255, blank=True, help_text="Target object representation")
    ip_address = models.GenericIPAddressField(null=True, blank=True, help_text="Client IP address")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Audit Log'
        verbose_name_plural = 'Audit Logs'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.action} by {self.user} at {self.created_at}"
