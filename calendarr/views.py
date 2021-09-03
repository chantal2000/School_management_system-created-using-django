from django.shortcuts import get_object_or_404, redirect, render
from .models import Event
from .forms import EventForm
# Create your views here.
from datetime import date, datetime
from django.shortcuts import render
from django.views import generic
from django.utils.safestring import mark_safe
from .models import *
from .utils import Calendar
class CalendarView(generic.ListView):
    model = Event
    template_name = 'event.htm'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('day', None))
        cal = Calendar(d.year, d.month)
        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        return context
def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()
def event(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()
    form = EventForm(request.POST,request.FILES or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return redirect('events:calendar')
    return render(request, 'calendarform.htm', {'form': form})
def event_profile(request,id):
    event=Event.objects.get(id=id)
    return render(request,"event_profile.htm",{"event":event})
def edit_event(request,id):
        event=Event.objects.get(id=id)
        if request.method=="POST":
            form=EventForm(request.POST,instance=event)
            if form.is_valid():
                form.save()
                return redirect("event_profile",id=event.id)
            else:
                form=EventForm(instance=event)
                return render(request,"edit_event.htm",{"form":form})