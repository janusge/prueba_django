from django.urls import path, include
from rest_framework import routers
from school.views.student import StudentView
from api.views.student_viewset import StudentViewSet

router=routers.DefaultRouter()
router.register(r'students', StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]