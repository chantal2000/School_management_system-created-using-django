from django.urls import path
from .views import *
urlpatterns=[path("register/",register_student, name="register_student"),
            path("list/",student_list,name="student_list"),
            path("profile/<int:id>/",student_profile,name="student_profile"),
            path("edit/<int:id>/",edit_student,name="edit_student"),
]# from django.urls import path
# from . import views 

# app_name='student'
# urlpatterns = [
#     path('All/',views.homepage,name="homepage"),
#     path('register/',views.register_student,name="register_student"),
#     path("list/",views.student_list,name="student_list"),
#     path("profile/<int:id>/",views.student_profile,name="student_profile"),
#     path("edit/<int:id>",views.edit_student,name="edit_student"),
# ]
