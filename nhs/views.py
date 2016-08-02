from django.shortcuts import *
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html', {})
