from django.contrib import admin

# Register your models here.
from .models import Event

class EventModelAdmin(admin.ModelAdmin):
    list_display = ["__str__", "start"]
    search_fields = ["name", "description"]
    class Meta:
        model = Event

admin.site.register(Event, EventModelAdmin)
