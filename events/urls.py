from django.conf.urls import url, include

from .views import *

app_name='events'
urlpatterns = [
    url(r'^$', EventListView.as_view(), name='list'),
    url(r'^your_events$', YourEventsListView.as_view(), name='your_events'),
    url(r'^attending$', attending, name='attending'),
    url(r'^(?P<pk>\d+)/$', EventDetailView.as_view(), name="detail")
]
