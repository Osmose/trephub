from django.conf.urls.defaults import patterns, url

from trephub.events import views


urlpatterns = patterns('',
    url(r'^/?$', views.event_list, name='trephub.events.list'),
)
