from django.shortcuts import render

# Create your views here.
from .serializers import StudentSerializers,TrainerSerializers,CourseSerializers,EventSerializers

from rest_framework import viewsets
from student.models import Student
from trainer.models import Trainer
from course.models import Course
from calendarr.models import Event

class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers

class TrainerViewSet(viewsets.ModelViewSet):
    queryset=Trainer.objects.all()
    serializer_class=TrainerSerializers
class CourseViewSet(viewsets.ModelViewSet):
    queryset=Course.objects.all()
    serializer_class=CourseSerializers
class EventViewSet(viewsets.ModelViewSet):
    queryset=Event.objects.all()
    serializer_class=EventSerializers
