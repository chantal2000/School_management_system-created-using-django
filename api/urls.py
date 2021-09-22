from django.urls import path,include
from rest_framework import routers
from .views import StudentViewSet,TrainerViewSet,CourseViewSet,EventViewSet
router=routers.DefaultRouter()
router.register(r"student",StudentViewSet)
router.register(r"trainer",TrainerViewSet)
router.register(r"course",CourseViewSet)
router.register(r"calendar",EventViewSet)
urlpatterns =[
    path("",include(router.urls))
]
