from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
from school.entities.student import Student

class StudentView(object):

    def index(request):
        data = list(Student.objects.values())
        
        return JsonResponse(data, safe=False)

    def subjects(request, id):
        student = Student.objects.filter(id__exact=id).get()
        data = list(student.subjects.values())
        
        return JsonResponse(data, safe=False)
