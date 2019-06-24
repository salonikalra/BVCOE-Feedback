from django.contrib import admin

from . import models

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['department_id', 'department_name']

class TeacherAdmin(admin.ModelAdmin):
    list_filter = ['department']
    list_display = ['teacher_name', 'teacher_id', 'get_subjects']
    search_fields = ['teacher_name', 'teacher_id']

    def get_subjects(self, obj):
        return ", ".join([s.subject_name for s in obj.subject_set.all()])
    get_subjects.short_description = 'subjects'

class SubjectAdmin(admin.ModelAdmin):
    list_filter = ['semester', 'department']
    list_display = ['subject_code', 'subject_name', 'get_teachers']
    search_fields = ['subject_code', 'subject_name']

    def get_teachers(self, obj):
        return ", ".join([t.teacher_name for t in obj.teacher.all()])
    get_teachers.short_description = 'teachers'

class feedbackAdmin(admin.ModelAdmin):
    list_display = ['student', 'teacher', 'subject', 'total', 'average']
    list_select_related = ['student', 'teacher', 'subject']
    search_fields = ['student__user__username', 'teacher__teacher_name', 'subject__subject_name']

admin.site.register(models.Department, DepartmentAdmin)
admin.site.register(models.Semester)
admin.site.register(models.Teacher, TeacherAdmin)
admin.site.register(models.Subject, SubjectAdmin)
admin.site.register(models.feedback, feedbackAdmin)
