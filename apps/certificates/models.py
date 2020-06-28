from django.db import models
from apps.utils.models import AbstractTableMeta


# Create your models here.
class Certificate(AbstractTableMeta, models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
