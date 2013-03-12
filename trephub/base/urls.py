from django.conf.urls.defaults import patterns, url

from trephub.base import views


urlpatterns = patterns('',
    url(r'^$', views.home, name='trephub.base.home'),
    url(r'^meetup/$', views.meetup_events, name='trephub.base.meetup'),
    url(r'^sponsors/$', views.sponsors, name='trephub.base.sponsors'),
    url(r'^about/$', views.about, name='trephub.base.about'),
)
