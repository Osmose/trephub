from django.shortcuts import render

from trephub.base import meetup


def home(request):
    return render(request, 'base/home.html')


def meetup_events(request):
    events = meetup.events()
    return render(request, 'base/meetup.html', {'events': events})
