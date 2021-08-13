from django.urls import path
from .views import register_course
urlpatterns = [
    path('registercourse/',register_course,name="register_course"),
]
