from django.db import models
from datetime import datetime
from django_countries.fields import CountryField
from django.db.models.fields import PositiveBigIntegerField
from phonenumber_field.modelfields import PhoneNumberField

class Trainer(models.Model):
    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=12)
    country =CountryField()
    date_of_birth = models.DateTimeField(default=datetime.now)
    trainer_id=models.PositiveSmallIntegerField(default=1)
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
    # email_address=models.EmailField(max_length=30)
    profile_image=models.ImageField()
    course_name=models.CharField(max_length=30)
    languages=models.CharField(max_length=30,choices=LANGUAGES)
    


    
   



    
   