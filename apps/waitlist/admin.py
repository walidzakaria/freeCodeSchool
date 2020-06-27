from django.contrib import admin

# Register your models here.
from .models import WaitlistEntry


class WaitListEntryAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'created_at', 'updated_at',)
    search_fields = ('first_name', 'last_name',)


admin.site.register(WaitlistEntry, WaitListEntryAdmin)
