from django.db import models
from datetime import datetime
import datetime
datetime.datetime.now()

from django_countries.fields import CountryField
from django.db.models.fields import PositiveBigIntegerField
from phonenumber_field.modelfields import PhoneNumberField

class Student(models.Model):
    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=12)
    profile_image=models.ImageField()
    email_address=models.EmailField(max_length=30)
    country =CountryField()

    age=models.PositiveSmallIntegerField()
    date_of_birth = models.DateTimeField(blank=True,null=True)
    roll_number=models.CharField(max_length=5)
    student_id=models.PositiveSmallIntegerField(default=1)
    national_Id=models.CharField(max_length=16)
    CHOICES=(
        ('F',"Female"),
        ('M',"Male")
    )
    LANGUAGES=(
        ('k',"kinyarwanda"),
        ('E',"English"),
        ('L',"Luganda"),
        ('k',"kiswahili"),
    )
    gender=models.CharField(max_length=10,choices=CHOICES)
    phone_number=PhoneNumberField() 
    guardian_name=models.CharField(max_length=40)
    gender=models.CharField(max_length=10,choices=CHOICES)
    grade=models.CharField(max_length=2)
    medical_report=models.FileField(upload_to='uploads/%Y/%m/%d')
    date_Of_enrollment=models.DateTimeField(blank=True,null=True)
    course_name=models.CharField(max_length=30)
    laptop_number=models.CharField(max_length=7)
    languages=models.CharField(max_length=30,choices=LANGUAGES)
    laptop_serial_number=models.CharField(max_length=20,blank=True,null=True)
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    def year_of_birth(self):
        current_year=datetime.datetime.now().year
        return current_year-self.age   


    


    
   



    
   