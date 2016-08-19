from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime

class Event(models.Model):
    name = models.CharField(max_length=100)
    start = models.DateTimeField()
    end = models.DateTimeField()
    description = models.TextField()
    location = models.CharField(max_length=100)
    contact_name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=100)
    attendees = models.ManyToManyField(User, through='Attendee')
    #timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    
    def __str__(self):
        return self.name
        
    def same_day(self):
        return self.start.day == self.end.day
        
    def hours(self):
        timedelta = self.end - self.start
        hours = timedelta.seconds / 60 / 60
        hours = round(hours * 2) / 2.0
        return hours
        
class Attendee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)
    date_joined = models.DateField(default=timezone.now)
    
    
    def hours(self):
        return 0
        
    def approved_hours(self):
        return 0
#class Attendee look for 'foreign key'
