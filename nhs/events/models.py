from django.db import models

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