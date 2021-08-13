from django import forms
from django.db.models import fields
from .models import Trainer
class TrainerRegistrationForm(forms.ModelForm):
    class Meta():
        model=Trainer
        fields=("__all__")
        widgets={
        'first_name':forms.TextInput(attrs={'class':'form_control'}),
        'last_name':forms.TextInput(attrs={'class':'form_control'}),
        'biography':forms.Textarea(attrs={'class':'form_control1'}),
        'age':forms.NumberInput(attrs={'class':'form_control'}),
        'date_of_birth':forms.DateTimeInput(attrs={'class':'form_control'}),
        'country':forms.Select(attrs={'class':'form_control'}),
        'date_hired':forms.DateTimeInput(attrs={'class':'form_control'}),
        'trainer_id':forms.TextInput(attrs={'class':'form_control'}),
        'national_Id':forms.NumberInput(attrs={'class':'form_control'}),
        'gender':forms.Select(attrs={'class':'form_control'}),
        'phone_number':forms.NumberInput(attrs={'class':'form_control'}),
        'email_address':forms.EmailInput(attrs={'class':'form_control'}),
        'profile_image':forms.FileInput(attrs={'class':'form_control'}),
        'course_name':forms.TextInput(attrs={'class':'form_control'}),
        'contract':forms.FileInput(attrs={'class':'form_control'}),
        'class_name':forms.TextInput(attrs={'class':'form_control'}),
        'languages':forms.Select(attrs={'class':'form_control'}),
        }
        
        

        