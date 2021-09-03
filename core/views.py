from django.shortcuts import render

# Create your views here.

from student.models import *
from trainer.models import *
from course.models import *
from calendarr.models import *

def home(request):
    students=Student.objects.count()
    trainers=Trainer.objects.count()
    courses=Course.objects.count()
    events=Event.objects.count()
    data={"students":students,"trainers":trainers,"courses":courses,"events":events}
    return render(request,"home.htm",data)

