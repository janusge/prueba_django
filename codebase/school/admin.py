from django.contrib import admin
from .entities.student import Student
from .entities.teacher import Teacher
from .entities.subject import Subject


class StudentAdmin(admin.ModelAdmin):
    fields = [
        'name',
        'last_name',
        'subjects'
    ]

admin.site.register(Student, StudentAdmin)


class TeacherAdmin(admin.ModelAdmin):
    fields = [
        'name',
        'last_name',
        'subjects'
    ]

admin.site.register(Teacher, TeacherAdmin)

class SubjectAdmin(admin.ModelAdmin):
    fields = [
        'name'
    ]

admin.site.register(Subject, SubjectAdmin)