from django.urls import path
from .views import *
urlpatterns = [
    path('home/',homepage,name="homepage"),
    path('register/',register_student,name="register_student"),
    path("list/",student_list,name="student_list"),
   
]


