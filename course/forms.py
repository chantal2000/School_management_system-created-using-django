from django import forms
from django.db.models import fields
from .models import Course
class CourseRegistrationForm(forms.ModelForm):
    class Meta():
        model=Course
        fields=("__all__")
        widgets={
        'course_name':forms.TextInput(attrs={'class':'form_control'}),
        'course_code':forms.TextInput(attrs={'class':'form_control'}),
        'course_duration':forms.DateTimeInput(attrs={'class':'form_control'}),
        'trainer_name':forms.TextInput(attrs={'class':'form_control'}),
        'time_in_hours':forms.TextInput(attrs={'class':'form_control'}),
        'syllabus':forms.FileInput(attrs={'class':'form_control'}),
        'course_duration':forms.TextInput(attrs={'class':'form_control'}),
        'course_schedule':forms.FileInput(attrs={'class':'form_control'})
        
        }

        