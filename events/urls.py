from django.conf.urls import url

from .views import EventListView, EventDetailView, attending

app_name='events'
urlpatterns = [
    url(r'^$', EventListView.as_view(), name='list'),
    url(r'^attending$', attending, name='attending'),
    url(r'^(?P<pk>\d+)/$', EventDetailView.as_view(), name="detail")
]
