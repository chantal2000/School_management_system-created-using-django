from django.db import models
from datetime import datetime
from django_countries.fields import CountryField
from django.db.models.fields import PositiveBigIntegerField
from phonenumber_field.modelfields import PhoneNumberField
from django.conf.global_settings import LANGUAGES

class Student(models.Model):
    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=12)
    country =CountryField()
    age=models.PositiveSmallIntegerField()
    languages = models.CharField(max_length=7, choices=LANGUAGES)
    date_of_birth = models.DateTimeField(default=datetime.now)
    roll_number=models.CharField(max_length=5)
    student_id=models.PositiveSmallIntegerField(default=1)
    national_Id=models.CharField(max_length=16)
    CHOICES=(
        ('F',"Female"),
        ('M',"Male")
    )
  
    gender=models.CharField(max_length=10,choices=CHOICES)
    phone_number=PhoneNumberField() 
    guardian_name=models.CharField(max_length=40)
    email_address=models.EmailField(max_length=30)
    gender=models.CharField(max_length=10,choices=CHOICES)
    profile_image=models.ImageField()
    grade=models.CharField(max_length=2)
    medical_report=models.FileField(upload_to='uploads',blank=True)
    date_Of_enrollment=models.DateTimeField(default=datetime.now)
    course_name=models.CharField(max_length=30)
    laptop_number=models.CharField(max_length=7)
    laptop_serial_number=models.CharField(max_length=20,blank=True,null=True)
    



    
   



    
   