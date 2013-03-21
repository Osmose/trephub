from datetime import datetime

from django.core.urlresolvers import reverse
from django.db import models

from easy_thumbnails.fields import ThumbnailerImageField

from trephub.base.models import CountryField


class Location(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, blank=True)
    postal_code = models.CharField(max_length=64, blank=True)
    country = CountryField()

    def __unicode__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(default='', unique=True)

    start = models.DateTimeField(blank=True, null=True)
    end = models.DateTimeField(blank=True, null=True)
    location = models.ForeignKey(Location)
    attendance = models.PositiveIntegerField(
        help_text='Number of people who attended the event.')

    summary = models.TextField(default='',
                               help_text=('Short paragraph summarizing the '
                                          'event.'))
    details = models.TextField(default='', blank=True,
                               help_text=('Optional longer description of the '
                                          'event.'))

    created = models.DateTimeField(default=datetime.now)
    updated = models.DateTimeField()

    def save(self, *args, **kwargs):
        self.updated = datetime.now()
        return super(Event, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('events.details.slug', args=[self.slug])

    def __unicode__(self):
        return u'<Event `{0}`>'.format(self.name)


class Photo(models.Model):
    event = models.ForeignKey(Event)

    created = models.DateTimeField(default=datetime.now)
    updated = models.DateTimeField()

    def _image_path(self, filename):
        return 'events/{0}/photos/{1}'.format(self.event.id, filename)
    image = ThumbnailerImageField(upload_to=_image_path)

    def save(self, *args, **kwargs):
        self.updated = datetime.now()
        return super(Photo, self).save(*args, **kwargs)

    def __unicode__(self):
        return u'<Photo ({0}): `{1}`>'.format(self.event.name, self.image)


class EventFile(models.Model):
    event = models.ForeignKey(Event)
    name = models.CharField(max_length=255)

    created = models.DateTimeField(default=datetime.now)
    updated = models.DateTimeField()

    def _file_path(self, filename):
        return 'events/{0}/files/{1}'.format(self.event.id, filename)
    file = models.FileField(upload_to=_file_path)

    def save(self, *args, **kwargs):
        self.updated = datetime.now()
        return super(EventFile, self).save(*args, **kwargs)

    def __unicode__(self):
        return u'<EventFile ({0}): `{1}`>'.format(self.event.name, self.file)
