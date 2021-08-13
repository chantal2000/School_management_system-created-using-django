from django import forms
from django.db.models import fields
from .models import Event
class EventRegistrationForm(forms.ModelForm):
    class Meta():
        model=Event
        fields=("__all__")
        widgets={
        'venue':forms.TextInput(attrs={'class':'form_control'}),
        'event_name':forms.TextInput(attrs={'class':'form_control'}),
        'age':forms.NumberInput(attrs={'class':'form_control'}),
        'event_planner':forms.TextInput(attrs={'class':'form_control'}),
        'event_duration':forms.TextInput(attrs={'class':'form_control'}),
        'event_approval':forms.NumberInput(attrs={'class':'form_control'}),
        'event_participants':forms.Textarea(attrs={'class':'form_control1'}),
        'event_date':forms.DateInput(attrs={'class':'form_control'}),
        'event_time':forms.TimeInput(attrs={'class':'form_control'}),
        'event_description':forms.Textarea(attrs={'class':'form_control1'}),
        'event_id':forms.TextInput(attrs={'class':'form_control'}),
  
        }

        