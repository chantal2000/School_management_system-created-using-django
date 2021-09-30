from school_system.trainer.views import delete_trainer
from django.urls import path
from . import views 
urlpatterns = [
    path('registercourse/',views.register_course,name="register_course"),
    path("list/",views.course_list,name="course_list"),
    path("profile/<int:id>",views.course_profile,name="course_profile"),
    path("edit/<int:id>",views.edit_course,name="edit_course"),
    path("delete/<int:id>",views.delete_course,name="delete_course"),
    path('home/',views.home_course,name="home_course")

]
