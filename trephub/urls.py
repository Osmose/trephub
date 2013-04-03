from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.http import HttpResponse
from django.shortcuts import render
from django.views.defaults import page_not_found

from funfactory.monkeypatches import patch

from trephub.monkeypatches import patch as trephub_patch

patch()
trephub_patch()
admin.autodiscover()


def handler500(request):
    return render(request, '500.html')


def robots_txt(request):
    return HttpResponse(
        'User-agent: *\n%s: /' % 'Allow' if settings.ENGAGE_ROBOTS else 'Disallow',
        mimetype="text/plain"
    )


urlpatterns = patterns('',
    (r'', include('trephub.base.urls')),
    (r'^events/', include('trephub.events.urls')),
    (r'^blog/', include('trephub.blog.urls')),

    # Generate a robots.txt
    (r'^robots\.txt$', robots_txt),

    (r'^admin/', include(admin.site.urls)),
)


## In DEBUG mode, serve media files through Django.
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^404$', page_not_found),
        (r'^500$', handler500),
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    ) + staticfiles_urlpatterns()
