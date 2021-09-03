from django.conf.urls import url
from . import views 
urlpatterns = [
    url('registerevent/',views.CalendarView.as_view(),name='calendar'),
    url('eventform/',views.event,name='eventform'),
    url("profile/<int:id>/",views.event_profile,name="course_profile"),
    url("edit/<int:id>/",views.edit_event,name="edit_course"),
]
