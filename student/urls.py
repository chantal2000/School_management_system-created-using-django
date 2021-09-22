from django.urls import path
from .views import *
# app_name='student'
urlpatterns=[
            path("register/",register_student, name="register_student"),
            path("list/",student_list,name="student_list"),
            path("profile/<int:id>/",student_profile,name="student_profile"),
            path("edit/<int:id>/",edit_student,name="edit_student"),
            path('home/',home_student,name="home_student"),
            path('all/',all_students,name="all_students"),
            path('login/',login,name="login")

]
