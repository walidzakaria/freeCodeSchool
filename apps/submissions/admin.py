from django.contrib import admin
from .models import StudentSubmission


# Register your models here.
class AdminStudentSubmission(admin.ModelAdmin):
    list_display = ('get_student', 'get_project', 'approved')
    list_filter = ('project__title',)
    search_fields = ('student__name',)

    # to refer to foreign data
    def get_project(self, obj):
        return obj.project.title

    get_project.admin_order_field = 'project'
    get_project.short_description = 'Project Title'

    def get_student(self, obj):
        return obj.student.email

    get_student.admin_order_field = 'student'
    get_student.short_description = 'Student\'s Name'


admin.site.register(StudentSubmission, AdminStudentSubmission)