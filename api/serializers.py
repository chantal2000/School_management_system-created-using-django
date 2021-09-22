from rest_framework import serializers

from student.models import Student
from trainer.models import Trainer
from course.models import Course
from calendarr.models import Event

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=["first_name","last_name","age"]
class TrainerSerializers(serializers.ModelSerializer):
    class Meta:
        model=Trainer
        fields=["first_name","last_name"]
class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields=["course_name","trainer_name"]
class EventSerializers(serializers.ModelSerializer):
    class Meta:
        model=Event
        fields=["event_id","title","start_time"]