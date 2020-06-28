from django.contrib import admin
from .models import Projects


# Register your models here.
class AdminProjects(admin.ModelAdmin):
    list_display = ('title', 'level', 'is_required')
    list_filter = ('level',)


admin.site.register(Projects, AdminProjects)