from django.db import models


class Staff(models.Model):
    school = models.ForeignKey(
        'schools.School',
        on_delete=models.CASCADE,
        related_name='staff_members',
        help_text="School where staff member is deployed"
    )
    staff_number = models.CharField(max_length=50, help_text="TSC Number or School Staff ID")
    full_name = models.CharField(max_length=255, help_text="Full legal name of the staff member")
    department = models.CharField(max_length=100, help_text="Department e.g. Mathematics, Sciences, Humanities, Boarding")
    phone = models.CharField(max_length=30, help_text="Primary phone number (e.g. +2547XXXXXXXX)")
    is_active = models.BooleanField(default=True, help_text="Active employment status")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('school', 'staff_number')
        verbose_name = 'Staff Member'
        verbose_name_plural = 'Staff Members'
        ordering = ['staff_number']

    def __str__(self):
        return f"{self.staff_number} - {self.full_name} ({self.department})"
