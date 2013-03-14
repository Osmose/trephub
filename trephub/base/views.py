from django.shortcuts import render

from trephub.base import meetup
from trephub.base.models import Sponsor
from trephub.blog.models import BlogEntry


def home(request):
    try:
        blog_entry = BlogEntry.objects.latest('published')
    except BlogEntry.DoesNotExist:
        blog_entry = None
    sponsors = Sponsor.objects.all()
    events = meetup.events()[:3]
    return render(request, 'base/home.html', {
        'sponsors': sponsors,
        'events': events,
        'blog_entry': blog_entry
    })


def meetup_events(request):
    events = meetup.events()
    return render(request, 'base/meetup.html', {'events': events})


def sponsors(request):
    sponsors = Sponsor.objects.all()
    return render(request, 'base/sponsors.html', {'sponsors': sponsors})


def about(request):
    return render(request, 'base/about.html')
