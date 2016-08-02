from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    name = models.CharField(max_length=100)
    start = models.DateTimeField()
    end = models.DateTimeField()
    description = models.TextField()
    location = models.CharField(max_length=100)
    contact_name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=100)
    #timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    
    def __str__(self):
        return self.name
        
    def same_day(self):
        if start.day == end.day:
            return true;
        else:
            return false;
        
    def hours(self):
        timedelta = end - start
        hours = timedelta.seconds / 60 / 60
        return hours
        
class Attendee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)
    date_joined = models.DateField()
    
    def hours(self):
        return event.hours();
        
    def approved_hours(self):
        return 0
#class Attendee look for 'foreign key'
