from django.urls import path
from .views import register_trainer
urlpatterns = [
    path('registertrainer/',register_trainer,name="register_trainer"),
]
