from django.shortcuts import render

from trephub.base import meetup
from trephub.base.models import Sponsor


def home(request):
    sponsors = Sponsor.objects.all()
    return render(request, 'base/home.html', {
        'sponsors': sponsors
    })


def meetup_events(request):
    events = meetup.events()
    return render(request, 'base/meetup.html', {'events': events})


def sponsors(request):
    sponsors = Sponsor.objects.all()
    return render(request, 'base/sponsors.html', {'sponsors': sponsors})
