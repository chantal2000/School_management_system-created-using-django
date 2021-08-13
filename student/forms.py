from django import forms
from django.db.models import fields
from .models import Student
class StudentRegistrationForm(forms.ModelForm):
    class Meta():
        model=Student
        fields=("__all__")
        widgets={
        'first_name':forms.TextInput(attrs={'class':'form_control'}),
        'last_name':forms.TextInput(attrs={'class':'form_control'}),
        'age':forms.NumberInput(attrs={'class':'form_control'}),
        'date_of_birth':forms.DateTimeInput(attrs={'class':'form_control'}),
        'roll_number':forms.TextInput(attrs={'class':'form_control'}),
        'student_id':forms.NumberInput(attrs={'class':'form_control'}),
        'national_Id':forms.TextInput(attrs={'class':'form_control'}),
        'gender':forms.Select(attrs={'class':'form_control'}),
        'phone_number':forms.NumberInput(attrs={'class':'form_control'}),
        'guardian_name':forms.TextInput(attrs={'class':'form_control'}),
        'email_address':forms.EmailInput(attrs={'class':'form_control',}),
        'country':forms.Select(attrs={'class':'form_control'}),
        'profile_image':forms.FileInput(attrs={'class':'form_control'}),
        'grade':forms.TextInput(attrs={'class':'form_control'}),
        'medical_report':forms.FileInput(attrs={'class':'form_control'}),
        'date_Of_enrollment':forms.DateInput(attrs={'class':'form_control'}),
        'course_name':forms.TextInput(attrs={'class':'form_control'}),
        'laptop_number':forms.NumberInput(attrs={'class':'form_control'}),
        'languages':forms.Select(attrs={'class':'form_control'}),
        'laptop_serial_number':forms.TextInput(attrs={'class':'form_control'}),

        }
        

        