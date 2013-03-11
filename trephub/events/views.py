from django.shortcuts import render

from trephub.events.models import Event


def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/list.html', {'events': events})
