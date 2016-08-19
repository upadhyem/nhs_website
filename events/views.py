from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import *
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_POST
from django.urls import reverse


from .models import Event, Attendee

# Create your views here.
def index(request):
    return render(request, 'events/index.html', {})

@login_required
@require_POST
def attending(request):
    user = request.user
    event_id = request.POST['event_id']
    event = Event.objects.get(pk=event_id)
    action = request.POST['action']
    if action == 'Leave' and user in event.attendees.all():
        a = Attendee.objects.get(user=user, event = event)
        a.delete()
    elif action == 'Join' and not user in event.attendees.all():
        a = Attendee(user=user, event=event)
        a.save()
    return HttpResponseRedirect(reverse('events:detail', kwargs={'pk': event_id}))   
    
class EventListView(ListView):
    model = Event
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(EventListView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        hours = 0
        for e in self.get_queryset():
            hours += e.hours()
        context['hours'] = round(hours * 2) / 2.0
        return context
    
class EventDetailView(DetailView):
    template_name = "events/detail.html"
    model = Event
    
  
class YourEventsListView(ListView):
    template_name = "events/event_list.html"
    model = Event
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):        
        return super(ListView, self).dispatch(request, *args, **kwargs)
    
    def get_queryset(self):
        return Event.objects.filter(attendees = self.request.user)
        
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(YourEventsListView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        hours = 0
        for e in self.get_queryset():
            hours += e.hours()
        context['hours'] = round(hours * 2) / 2.0
        return context
    
    
