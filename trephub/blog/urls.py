from django.conf.urls.defaults import patterns, url

from trephub.blog import views


urlpatterns = patterns('',
    url(r'^$', views.BlogEntryList.as_view(), name='blog.list'),
    url(r'^(?P<slug>[\w-]+)/$', views.BlogEntryDetail.as_view(),
        name='blog.details.slug'),
    url(r'^(?P<pk>\d+)/$', views.BlogEntryDetail.as_view(),
        name='blog.details.pk'),
)
