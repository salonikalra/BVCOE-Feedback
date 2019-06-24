from django.contrib import admin
from .models import Student

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_filter = ['semester', 'department']
    list_display = ['user', 'semester', 'department']
    list_select_related = ['user']
    search_fields = ['user__username']

admin.site.register(Student, StudentAdmin)
