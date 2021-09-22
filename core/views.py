from django.shortcuts import render
from student.models import Student
from trainer.models import Trainer
from course.models import Course
from calendarr.models import Event
def home(request):
    students=Student.objects.count(),
    trainers=Trainer.objects.count(),
    courses=Course.objects.count(),
    events=Event.objects.count(),
    data={'student':students,'trainer':trainers,'course':courses,'event':events}
    return render(request,'home_page.htm',data)