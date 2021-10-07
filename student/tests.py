from django.conf.urls import url
from django.test import TestCase
import datetime
from django.urls import reverse

# Create your tests here.
from .models import Student
class StudentModelTestCase(TestCase):
    def setUp(self):
        self.student=Student(first_name="Chantal",last_name="Niyonkuru",age=20,country="Rwanda",course_name="Python",grade="A",email_address="nniyonkuruchantal@gmail.com",guardian_name="Kampire")
    def test_fulname_contains_first_name(self):
        self.assertIn(self.student.first_name,self.student.full_name())
    def test_fulname_contains_last_name(self):
        self.assertIn(self.student.last_name,self.student.full_name())

    def test_year_of_birth(self):
        current_year=datetime.datetime.now().year
        year=current_year-self.student.age
        self.assertEqual(year,self.student.year_of_birth())

    def test_register_student_view(self):
        url=reverse('register_student')
        data={"first_name":self.student.first_name,
        "last_name":self.student.last_name,
        "age":self.student.age,
        "country":self.student.country,
        "course_name":self.student.course_name,
        }
        request=self.client.post(url,data)
        self.assertEqual(request.status_code,200)
    



