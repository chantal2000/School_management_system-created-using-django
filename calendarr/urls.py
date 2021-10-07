from django.conf.urls import url
from . import views 
urlpatterns = [
    url('registerevent/',views.CalendarView.as_view(),name='calendar'),
    url('eventform/',views.event,name='eventform'),
    url("list/",views.event_list,name="event_list"),
    url("profile/<int:id>/",views.event_profile,name="event_profile"),
    url('home/',views.home_events,name="home_events"),
    url("edit/<int:id>/",views.edit_event,name="edit_event"),
    url("event_new/", views.event_form, name='event_new'),
    url("delete_event/", views.delete_event, name='delete_event'),

]
