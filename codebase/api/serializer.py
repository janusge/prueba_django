from rest_framework import serializers
from school.entities.student import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'
