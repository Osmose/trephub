from datetime import datetime

from django.conf import settings

import requests
from pyquery import PyQuery as pq


API_ROOT = 'https://api.meetup.com'


class MeetupServiceError(Exception):
    def __init__(self, exc):
        self.exc = exc


def _meetup_request(path, method='get', **kwargs):
    """Make a request to the Meetup API."""
    kwargs.setdefault('key', settings.MEETUP_API_KEY)
    param_key = 'params' if method == 'get' else 'data'

    try:
        response = requests.request(method, API_ROOT + path,
                                    **{param_key: kwargs})
    except requests.exceptions.RequestException as e:
        raise MeetupServiceError(e)

    return response.json()


def events():
    """Retrieve a list of events for the meetup group."""
    results = _meetup_request('/2/events',
                              group_urlname=settings.MEETUP_GROUP_URLNAME)
    events = results['results']

    # Annotate events with extra info.
    for event in events:
        event['time'] = datetime.fromtimestamp(int(event['time']) / 1000)

        # Pull the text from the first <p> tag as the description.
        paragraphs = pq(event['description'])('p')
        event['summary'] = paragraphs[0].text if paragraphs else ''

    return events
