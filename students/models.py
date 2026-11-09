from django.db import models


class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    school = models.ForeignKey(
        'schools.School',
        on_delete=models.CASCADE,
        related_name='students',
        help_text="Enrolled school"
    )
    admission_number = models.CharField(max_length=50, help_text="Unique student admission number within school")
    full_name = models.CharField(max_length=255, help_text="Full legal name of the student")
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    class_name = models.CharField(max_length=50, help_text="Class level e.g. Form 1, Form 2, Form 3, Form 4")
    stream = models.CharField(max_length=50, help_text="Class stream e.g. North, South, East, West, Red, Blue")
    dorm = models.CharField(max_length=100, blank=True, help_text="Dormitory or hostel name for boarders")
    guardian_name = models.CharField(max_length=255, blank=True, help_text="Parent or primary guardian name")
    guardian_phone = models.CharField(max_length=30, blank=True, help_text="Parent/guardian phone for SMS alerts (e.g. +2547XXXXXXXX)")
    consent_given = models.BooleanField(
        default=False,
        help_text="Data Protection Act consent given for biometric processing"
    )
    consent_date = models.DateField(null=True, blank=True, help_text="Date biometric consent was recorded")
    is_active = models.BooleanField(default=True, help_text="Active student status")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('school', 'admission_number')
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
        ordering = ['admission_number']

    def __str__(self):
        return f"{self.admission_number} - {self.full_name} ({self.class_name} {self.stream})"
