from django.db import models
from django.db import models
import datetime
from datetime import datetime
# Create your models here.
class Course(models.Model):
    course_name=models.CharField(max_length=30)
    course_code=models.CharField(max_length=10)
    course_schedule=models.FileField()
    syllabus=models.FileField()
    course_duration=models.CharField(max_length=10)
    trainer_name=models.CharField(max_length=30)
    time_in_hours=models.DurationField()
    
