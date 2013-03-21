from django.conf.urls.defaults import patterns, url

from trephub.base import views


urlpatterns = patterns('',
    url(r'^$', views.home, name='base.home'),
    url(r'^meetup/$', views.meetup_events, name='base.meetup'),
    url(r'^sponsors/$', views.sponsors, name='base.sponsors'),
    url(r'^about/$', views.about, name='base.about'),
)
