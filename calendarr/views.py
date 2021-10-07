from django.shortcuts import get_object_or_404, redirect, render
from .models import Event
from .forms import EventForm
# Create your views here.
from datetime import date, datetime
from django.shortcuts import render
from django.views import generic
from django.utils.safestring import mark_safe
from datetime import datetime, timedelta, date
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.utils.safestring import mark_safe
import calendar
from .models import *
from .utils import Calendar
from .forms import EventForm
class CalendarView(generic.ListView):
    model = Event
    template_name = 'event.htm'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context
def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()
def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month
def event(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()
    form = EventForm(request.POST,request.FILES or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return redirect('calendar')
    return render(request, 'calendarform.htm', {'form': form})
def event_profile(request,id):
    event=Event.objects.get(id=id)
    return render(request,"event_profile.htm",{"event":event})
def home_events(request):
    return render(request,"all_ca.htm")
def edit_event(request,id):
    event=Event.objects.get(id=id)
    if request.method=="POST":
        form=EventForm(request.POST,instance=event)
        if form.is_valid():
            form.save()
        return redirect("event_profile",id=event.id)
    else:
        form=EventForm(instance=event)
        return render (request,"edit_event.htm",{"form":form})
def event_form(request):
    if request.method=="POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('event_form'))
        else:
            print(form.errors)
    else:
        form= EventForm()
    return render(request,"event_form.htm",{"form":form})
def events_list(request):
    events=Event.objects.all()
    return render(request,"event_list.htm",{"events":events})
# def edit_event(request,id):
#     event=Event.objects.get(id=id)
#     if request.method=="POST":
#         form=EventForm(request.POST,instance=event)
#         if form.is_valid():
#             form.save()
#         return redirect("event_profile",id=event.id)
#     else:
#         form=EventForm(instance=event)
#         return render (request,"edit_event.htm",{"form":form})
def delete_course(request,id):
    events=Event.objects.get(id=id)
    events.delete()
    return redirect("event_list")