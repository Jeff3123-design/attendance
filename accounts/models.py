from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Role(models.TextChoices):
        SUPER_ADMIN = 'SUPER_ADMIN', 'Super Administrator'
        SCHOOL_ADMIN = 'SCHOOL_ADMIN', 'School Administrator'
        TEACHER = 'TEACHER', 'Teacher'
        BURSAR = 'BURSAR', 'Bursar'

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.SCHOOL_ADMIN,
        help_text="User system role determining access permissions"
    )
    school = models.ForeignKey(
        'schools.School',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='users',
        help_text="Assigned school for multi-tenant scoping. Null for Super Admins."
    )

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['username']

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"

    @property
    def is_super_admin(self):
        return self.role == self.Role.SUPER_ADMIN or self.is_superuser

    @property
    def is_school_admin(self):
        return self.role == self.Role.SCHOOL_ADMIN

    @property
    def is_teacher(self):
        return self.role == self.Role.TEACHER

    @property
    def is_bursar(self):
        return self.role == self.Role.BURSAR
