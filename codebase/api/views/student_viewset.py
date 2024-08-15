from rest_framework import viewsets
from api.serializer import StudentSerializer
from school.entities.student import Student

class StudentViewSet(viewsets.ModelViewSet):
    queryset= Student.objects.all()
    serializer_class = StudentSerializer