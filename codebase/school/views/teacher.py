from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
from school.entities.teacher import Teacher

class TeacherView(object):

    def index(request):
        data = list(Teacher.objects.values())
        
        return JsonResponse(data, safe=False)

    def subjects(request, id):
        teacher = Teacher.objects.filter(id__exact=id).get()
        data = list(teacher.subjects.values())
        
        return JsonResponse(data, safe=False)

    def listWithSubjects(request):
        teachers = Teacher.objects.select_related().all()

        data = []
        
        for teacher in teachers:
            subjects = [subject.name for subject in teacher.subjects.all()]
            data.append({
                'id': teacher.id,
                'name': teacher.name + " " + teacher.last_name,
                'materias': subjects,
            })
        
        return JsonResponse(data, safe=False)