from datetime import datetime

from django.db import models

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
    name = models.CharField(max_length=255)
    attendance = models.PositiveIntegerField()
    location = models.ForeignKey(Location)
    summary = models.TextField()

    created = models.DateTimeField(default=datetime.now)
    updated = models.DateTimeField()

    def save(self, *args, **kwargs):
        self.updated = datetime.now()
        return super(Event, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


class Photo(models.Model):
    event = models.ForeignKey(Event)

    created = models.DateTimeField(default=datetime.now)
    updated = models.DateTimeField()

    def _image_path(self, filename):
        return 'events/{0}/photos/{1}'.format(self.event.id, filename)
    image = models.ImageField(upload_to=_image_path)

    def save(self, *args, **kwargs):
        self.updated = datetime.now()
        return super(Photo, self).save(*args, **kwargs)

    def __unicode__(self):
        return 'Photo ({0}): {1}'.format(self.event.name, self.image)


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
        return 'File ({0}): {1}'.format(self.event.name, self.file)
