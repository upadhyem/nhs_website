from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import *
from django.http import HttpResponse
from .models import Event

# Create your views here.
def index(request):
    return render(request, 'events/index.html', {})
    
class EventListView(ListView):
    model = Event
    
class EventDetailView(DetailView):
    template_name = "events/detail.html"
    model = Event
    
    
    
