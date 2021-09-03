from django.db import models

# Create your models here.
class Event(models.Model):
    event_id=models.PositiveSmallIntegerField(default=1)
    title=models.CharField(max_length=100)
    description=models.TextField()
    start_time=models.DateTimeField()
    end_time=models.DateTimeField()

    def __str__(self):
        return self.title
        

   



