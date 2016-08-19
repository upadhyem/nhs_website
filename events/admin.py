from django.contrib import admin

# Register your models here.
from .models import Event, Attendee

class CategoryInline(admin.TabularInline):
    model = Attendee
    extra = 0 

class EventModelAdmin(admin.ModelAdmin):
    inlines = (CategoryInline,)
    list_display = ["__str__", "start",]
    search_fields = ["name", "description"]
    class Meta:
        model = Event


admin.site.register(Event, EventModelAdmin)
admin.site.register(Attendee)
