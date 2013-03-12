from django.shortcuts import get_object_or_404, render

from trephub.events.models import Event


def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/list.html', {'events': events})


def event_details(request, param, lookup=None):
    event = get_object_or_404(Event, **{lookup: param})
    return render(request, 'events/details.html', {'event': event})
