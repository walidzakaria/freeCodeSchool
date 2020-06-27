from django.db import models
from apps.utils.models import Timestamps


# Create your models here.
class WaitlistEntry(Timestamps, models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True
    )
    notes = models.TextField()

    class Meta:
        verbose_name_plural = 'waitlist entries'
