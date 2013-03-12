from django.conf.urls.defaults import patterns, url

from trephub.events import views


urlpatterns = patterns('',
    url(r'^/?$', views.event_list, name='trephub.events.list'),
    url(r'^(\d+)/?$', views.event_details, {'lookup': 'id'},
        name='trephub.events.details.id'),
    url(r'^([-\w]+)/?$', views.event_details, {'lookup': 'slug'},
        name='trephub.events.details.slug'),
)
