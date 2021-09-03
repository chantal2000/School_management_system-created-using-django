from django.shortcuts import render,redirect
from .forms import CourseRegistrationForm
from .models import Course

# Create your views here.

def homepage(request):
    return render(request,"all.htm")
def register_course(request):
    if request.method=="POST":
        form=CourseRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form=CourseRegistrationForm()
    return render(request,"register_student.htm",{"form":form,"name":"Chantal"})
def course_list(request):
    courses=Course.objects.all()
    return render(request,"course_list.htm",{"courses":courses})
def course_profile(request,id):
    course=Course.objects.get(id=id)
    return render(request,"course_profile.htm",{"course":course})
def edit_course(request,id):
    course=Course.objects.get(id=id)
    if request.method=="POST":
        form=CourseRegistrationForm(request.POST,instance=course)
        if form.is_valid():
            form.save()
        return redirect("course_profile",id=course.id)
    else:
        form=CourseRegistrationForm(instance=course)
        return render (request,"edit_course.htm",{"form":form})
