from django.db import models
from datetime import datetime
from django_countries.fields import CountryField
from django.db.models.fields import PositiveBigIntegerField
from phonenumber_field.modelfields import PhoneNumberField
class Trainer(models.Model):
    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=12)
    country =CountryField()
    date_of_birth = models.DateTimeField(default=datetime.now,null=True)
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
    profile_image = models.ImageField(upload_to='profile_img', blank=True, null=True , default='profile_img/925667.jpg')
    course_name=models.CharField(max_length=30)
    languages=models.CharField(max_length=30,choices=LANGUAGES)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    


    
   



    
   