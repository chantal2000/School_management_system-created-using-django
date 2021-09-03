
from django.shortcuts import render,redirect
from .forms import StudentRegistrationForm
from django.shortcuts import render
from .models import Student
from .forms import StudentRegistrationForm
# Create your views here.

def homepage(request):
    return render(request,"all.htm")
def register_student(request):
    if request.method=="POST":
        form=StudentRegistrationForm(request.POST ,request.FILES)
        if form.is_valid():
            form.save()
        else:
            print (form.errors)
    else:
        form=StudentRegistrationForm()
    return render(request,"register_student.htm",{"form":form})
def student_list(request):
    students=Student.objects.all()
    return render(request,"student_list.htm",{"students":students})
def student_profile(request,id):
    student=Student.objects.get(id=id)
    return render(request,"student_profile.htm",{"student":student})
def edit_student(request,id):
    student=Student.objects.get(id=id)
    if request.method=="POST":
        form=StudentRegistrationForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
        return redirect("student_profile",id=student.id)
    else:
        form=StudentRegistrationForm(instance=student)
        return render (request,"edit_student.htm",{"form":form})



