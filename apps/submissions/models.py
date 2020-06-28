from django.db import models
from apps.projects.models import Projects
from django.contrib.auth import get_user_model


# Create your models here.
class StudentSubmission(models.Model):
    student = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    project = models.ForeignKey(Projects, on_delete=models.DO_NOTHING)
    url = models.CharField(max_length=255)
    feedback = models.TextField(blank=True, default='')
    approved = models.BooleanField(default=False)
