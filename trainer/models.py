from django.db import models
import datetime
from datetime import datetime
from django_countries.fields import CountryField
from django.db.models.fields import PositiveBigIntegerField
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Trainer(models.Model):
    first_name=models.CharField(max_length=12)
    last_name=models.CharField(max_length=12)
    country = CountryField()
    date_of_birth = models.DateTimeField(default=datetime.now)
    trainer_id=models.PositiveSmallIntegerField()
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
    languages=models.CharField(max_length=30,choices=LANGUAGES)
    gender=models.CharField(max_length=10,choices=CHOICES)
    phone_number=PhoneNumberField() 
    biography=models.TextField(max_length=2000)
    profile_image=models.ImageField()
    contract=models.ImageField()
    course_name=models.CharField(max_length=30)
    date_hired=models.DateField()
    class_name=models.CharField(max_length=30)