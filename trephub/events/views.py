from django.views.generic import DetailView, ListView

from trephub.events.models import Event


class EventList(ListView):
    model = Event
    paginate_by = 5
    context_object_name = 'events'
    template_name = 'events/list.html'


class EventDetail(DetailView):
    model = Event
    context_object_name = 'event'
    template_name = 'events/details.html'
