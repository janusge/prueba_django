from django.urls import path
from school.views.student import StudentView
from school.views.teacher import TeacherView

urlpatterns = [
    path('students/', StudentView.index, name='school.students.index'),
    path('students/subjects/<str:id>', StudentView.subjects, name='school.students.subjects'),
    path('teachers/subjects/<str:id>', TeacherView.subjects, name='school.teachers.subjects'),
    path('teachers/', TeacherView.listWithSubjects, name='school.teachers.list')
]