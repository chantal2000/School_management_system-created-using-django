from django.shortcuts import render,redirect
from .forms import TrainerRegistrationForm
from .models import Trainer
# Create your views here.

def home_trainer(request):
    return render(request,"all_tra.htm")
def login_trainer(request):
    return render(request,"login.htm")

def register_trainer(request):
    if request.method=="POST":
        form=TrainerRegistrationForm(request.POST ,request.FILES)
        if form.is_valid():
            form.save()
        else:
            print (form.errors)
    else:
        form=TrainerRegistrationForm()
    return render(request,"register_student.htm",{"form":form})
def trainer_list(request):
    trainers=Trainer.objects.all()
    return render(request,"trainer_list.htm",{"trainers":trainers})
def trainer_profile(request,id):
    trainer=Trainer.objects.get(id=id)
    return render(request,"trainer_profile.htm",{"trainer":trainer})
def edit_trainer(request,id):
    student=Trainer.objects.get(id=id)
    if request.method=="POST":
        form=TrainerRegistrationForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
        return redirect("student_profile",id=student.id)
    else:
        form=TrainerRegistrationForm(instance=student)
        return render (request,"edit_student.htm",{"form":form})
def delete_trainer(request,id):
    trainers=Trainer.objects.get(id=id)
    trainers.delete()
    return redirect("trainer_list")
