from django.urls import path
from .views import *
urlpatterns = [
    path('registertrainer/',register_trainer,name="register_trainer"),
    path("list/",trainer_list,name="trainer_list"),

]
