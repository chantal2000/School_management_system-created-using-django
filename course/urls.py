from django.urls import path
from .views import *
urlpatterns = [
    path('registercourse/',register_course,name="register_course"),
    path("list/",course_list,name="course_list"),

]
