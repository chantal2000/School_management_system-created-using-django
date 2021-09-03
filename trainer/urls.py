from django.urls import path
from .views import *

urlpatterns = [
    path('registertrainer/',register_trainer,name="register_trainer"),
    path("list/",trainer_list,name="trainer_list"),
    path("profile/<int:id>",trainer_profile,name="trainer_profile"),
    path("edit/<int:id>",edit_trainer,name="edit_trainer"),
]
