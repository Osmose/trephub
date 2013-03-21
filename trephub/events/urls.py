from django.conf.urls.defaults import patterns, url

from trephub.events import views


urlpatterns = patterns('',
    url(r'^$', views.EventList.as_view(), name='events.list'),
    url(r'^(?P<slug>[\w-]+)/$', views.EventDetail.as_view(),
        name='events.details.slug'),
    url(r'^(?P<pk>\d+)/$', views.EventDetail.as_view(),
        name='events.details.pk'),
)
