from django.db import models


class SmsLog(models.Model):
    STATUS_CHOICES = [
        ('SENT', 'Sent'),
        ('DELIVERED', 'Delivered'),
        ('FAILED', 'Failed'),
        ('PENDING', 'Pending'),
    ]

    school = models.ForeignKey(
        'schools.School',
        on_delete=models.CASCADE,
        related_name='sms_logs',
        help_text="Tenant school that dispatched the SMS"
    )
    recipient = models.CharField(max_length=50, help_text="Guardian or recipient phone number")
    message = models.TextField(help_text="SMS content delivered via Africa's Talking / Twilio gateway")
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'SMS Log'
        verbose_name_plural = 'SMS Logs'
        ordering = ['-created_at']

    def __str__(self):
        return f"SMS to {self.recipient} [{self.status}]"
