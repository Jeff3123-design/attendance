from django.db import models


class Device(models.Model):
    LOCATION_CHOICES = [
        ('gate', 'Main Gate'),
        ('dorm', 'Dormitory'),
        ('dining', 'Dining Hall'),
        ('classroom', 'Classroom Block'),
    ]

    school = models.ForeignKey(
        'schools.School',
        on_delete=models.CASCADE,
        related_name='devices',
        help_text="School campus where this device is installed"
    )
    name = models.CharField(max_length=100, help_text="Device label e.g. Gate 1 Terminal, Dorm A Reader")
    serial_number = models.CharField(max_length=100, unique=True, help_text="Hardware serial number from ZKTeco device")
    ip_address = models.GenericIPAddressField(null=True, blank=True, help_text="Local IP address or public static IP")
    location = models.CharField(max_length=50, choices=LOCATION_CHOICES, default='gate')
    last_seen = models.DateTimeField(null=True, blank=True, help_text="Last ADMS heartbeat/punch received")
    is_active = models.BooleanField(default=True, help_text="Whether this device is active for syncing")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Device'
        verbose_name_plural = 'Devices'
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.serial_number}) - {self.school.name}"
