from django.db import models


class AttendanceLog(models.Model):
    """Raw punch log recorded directly from ZKTeco biometric terminals."""
    school = models.ForeignKey(
        'schools.School',
        on_delete=models.CASCADE,
        related_name='attendance_logs',
        help_text="Tenant school where punch occurred"
    )
    device = models.ForeignKey(
        'devices.Device',
        on_delete=models.CASCADE,
        related_name='attendance_logs',
        help_text="ZKTeco device hardware terminal"
    )
    user_id = models.CharField(
        max_length=50,
        help_text="Biometric terminal User PIN / enrollment ID"
    )
    timestamp = models.DateTimeField(help_text="Exact biometric scan timestamp")
    punch_type = models.CharField(
        max_length=20,
        default='CHECK_IN',
        help_text="Punch state: CHECK_IN, CHECK_OUT, BREAK_OUT, BREAK_IN"
    )
    raw_payload = models.TextField(blank=True, help_text="Original ADMS/PUSH payload line")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('device', 'user_id', 'timestamp')
        verbose_name = 'Attendance Log'
        verbose_name_plural = 'Attendance Logs'
        ordering = ['-timestamp']

    def __str__(self):
        return f"PIN {self.user_id} @ {self.timestamp} ({self.device.name})"


class DailyAttendance(models.Model):
    """Aggregated daily attendance record per student."""
    class Status(models.TextChoices):
        PRESENT = 'PRESENT', 'Present'
        LATE = 'LATE', 'Late'
        ABSENT = 'ABSENT', 'Absent'
        EXCUSED = 'EXCUSED', 'Excused'

    school = models.ForeignKey(
        'schools.School',
        on_delete=models.CASCADE,
        related_name='daily_attendance_records',
        help_text="Tenant school"
    )
    student = models.ForeignKey(
        'students.Student',
        on_delete=models.CASCADE,
        related_name='daily_attendance_records',
        help_text="Enrolled student"
    )
    date = models.DateField(help_text="Date of attendance roll")
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PRESENT,
        help_text="Attendance status evaluated against school cutoff times"
    )
    first_in = models.TimeField(null=True, blank=True, help_text="First morning biometric scan time")
    last_out = models.TimeField(null=True, blank=True, help_text="Last evening departure biometric scan time")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('school', 'student', 'date')
        verbose_name = 'Daily Attendance'
        verbose_name_plural = 'Daily Attendance Records'
        ordering = ['-date', 'student']

    def __str__(self):
        return f"{self.student.full_name} ({self.date}): {self.status}"
