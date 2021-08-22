from django.conf.urls import url
from . import views 
urlpatterns = [
    url('registerevent/',views.CalendarView.as_view(),name='calendar'),
    url('eventform/',views.event,name='eventform'),
]
