from django.conf.urls import url

from .views import EventListView, EventDetailView

app_name='events'
urlpatterns = [
    url(r'^$', EventListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', EventDetailView.as_view(), name="detail")
]
