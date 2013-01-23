from django.conf import settings
from django.conf.urls.defaults import patterns, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.http import HttpResponse

from funfactory.monkeypatches import patch


patch()
admin.autodiscover()


def robots_txt(request):
    return HttpResponse(
        'User-agent: *\n%s: /' % 'Allow' if settings.ENGAGE_ROBOTS else 'Disallow',
        mimetype="text/plain"
    )


urlpatterns = patterns('',
    # Example:
    (r'', include('trephub.base.urls')),

    # Generate a robots.txt
    (r'^robots\.txt$', robots_txt),

    (r'^admin/', include(admin.site.urls)),
)

## In DEBUG mode, serve media files through Django.
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
