from django.urls import path
from .views import register_event
urlpatterns = [
    path('registerevent/',register_event,name="register_event"),
]
