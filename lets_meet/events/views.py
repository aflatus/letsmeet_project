from django.views.generic import View, ListView, UpdateView, DeleteView, CreateView, DetailView
from .models import Event

class EventList(ListView):
    model = Event
    template_name = 'events/list_of_events.html'
    #TODO list_of_events.html

class EventDisplay(DetailView):
    model = Event
    template_name = 'events/event_detail.html'
    #TODO event_detail.html

class EventCreate(CreateView):
    model = Event
    template_name = 'events/create.html'
    #TODO create.html


class EventUpdate(UpdateView):
    model = Event
    template_name = 'events/update.html'
    #TODO update.html


class EventDelete(DeleteView):
    model = Event
    template_name = 'events/delete.html'
    #TODO delete.html
