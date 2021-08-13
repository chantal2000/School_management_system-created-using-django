from django.db import models

# Create your models here.
class Event(models.Model):
    venue=models.CharField(max_length=12)
    event_id=models.CharField(max_length=20)
    event_name=models.CharField(max_length=30)
    event_duration=models.CharField(max_length=20)
    event_planner=models.CharField(max_length=30)
    event_approval=models.CharField(max_length=30)
    event_participants=models.TextField(max_length=50)
    event_date=models.DateField()
    event_time=models.TimeField()
    event_description=models.TextField(max_length=2000,default='Description' )
