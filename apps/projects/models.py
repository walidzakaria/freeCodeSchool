from django.db import models
from apps.utils.models import AbstractTableMeta


# Create your models here.
class Projects(AbstractTableMeta, models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, default='')
    url = models.CharField(max_length=255)
    level = models.IntegerField(choices=((1, 'Level 1'), (2, 'Level 2')),
                                default=1)
    is_required = models.BooleanField(default=True)
