from datetime import datetime

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models

from markupfield.fields import MarkupField


class BlogEntry(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(User)

    summary = MarkupField(markup_type='markdown')
    content = MarkupField(markup_type='markdown')

    is_public = models.BooleanField('Public?', default=False)

    created = models.DateTimeField(default=datetime.now)
    updated = models.DateTimeField()
    published = models.DateTimeField(blank=True)

    def __init__(self, *args, **kwargs):
        super(BlogEntry, self).__init__(*args, **kwargs)
        self.__original_is_public = self.is_public

    def save(self, *args, **kwargs):
        self.updated = datetime.now()

        # If is_public was set to true, we should update the published date.
        if self.is_public and not self.__original_is_public:
            self.published = datetime.now()

        return super(BlogEntry, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('trephub.blog.details.slug', kwargs={'slug': self.slug})

    def get_newer(self, **kwargs):
        entries = (
            BlogEntry.objects.filter(published__gt=self.published, **kwargs)
            .order_by('published')[:1]
        )
        return entries[0] if entries else None

    def get_older(self, **kwargs):
        entries = (
            BlogEntry.objects.filter(published__lt=self.published, **kwargs)
            .order_by('-published')[:1]
        )
        return entries[0] if entries else None

    def __unicode__(self):
        return u'<BlogEntry `{0}`>'.format(self.title)

    class Meta:
        verbose_name_plural = 'blog entries'
