from django.test import TestCase
from django.conf.urls import url
import datetime
from django.urls import reverse
from .models import Trainer

# Create your tests here.

class TrainerModelTestCase(TestCase):
    def setUp(self):
        self.trainer=Trainer(first_name="James",last_name="Mwai",country="Rwanda",course_name="Python",grade="A",email_address="smartemwa@gmail.com")
    def test_fulname_contains_first_name(self):
        self.assertIn(self.trainer.first_name,self.trainer.full_name())
    def test_fulname_contains_last_name(self):
        self.assertIn(self.trainer.last_name,self.trainer.full_name())

    def test_year_of_birth(self):
        current_year=datetime.datetime.now().year
        year=current_year-self.trainer.age
        self.assertEqual(year,self.trainer.year_of_birth())

    def test_register_trainer_view(self):
        url=reverse('register_trainer')
        data={"first_name":self.trainer.first_name,
        "last_name":self.trainer.last_name,
        "country":self.trainer.country,
        "course_name":self.trainer.course_name,
        }
        request=self.client.post(url,data)
        self.assertEqual(request.status_code,200)
    




