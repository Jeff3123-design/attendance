from django.db import models


class School(models.Model):
    name = models.CharField(max_length=255, help_text="Full name of the secondary school")
    code = models.CharField(max_length=50, unique=True, help_text="Unique school MOE code or registration number")
    county = models.CharField(max_length=100, help_text="Kenyan county e.g. Kiambu, Nairobi, Nakuru")
    phone = models.CharField(max_length=30, help_text="Official school administration phone")
    email = models.EmailField(help_text="Official school email address")
    logo = models.ImageField(upload_to='school_logos/', blank=True, null=True, help_text="School crest or logo")
    is_active = models.BooleanField(default=True, help_text="Whether this school tenant is active")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'School'
        verbose_name_plural = 'Schools'
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.code})"
