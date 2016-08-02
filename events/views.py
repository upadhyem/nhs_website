from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import *
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from .models import Event

# Create your views here.
def index(request):
    return render(request, 'events/index.html', {})

@login_required
@require_POST
def attending(request):
    return HttpResponse("<h1>Joined!</h1>")
    #return render(request, 'events/index.html', {})
    
class EventListView(ListView):
    model = Event
    
class EventDetailView(DetailView):
    template_name = "events/detail.html"
    model = Event
    
    
    
