import os

from django.core.urlresolvers import reverse
from django.db import models
from django.template.defaultfilters import slugify

from product_details import product_details


ENGLISH_COUNTRY_CHOICES = sorted(
    [(code, u'{0} ({1})'.format(name, code)) for code, name in
     product_details.get_regions('en-US').items()],
    cmp=lambda x, y: cmp(x[1], y[1])
)


class CountryField(models.CharField):
    description = ('CharField with country settings specific to trephub '
                   'defaults.')

    def __init__(self, *args, **kwargs):
        options = {
            'max_length': 16,
            'default': u'us',
            'choices': ENGLISH_COUNTRY_CHOICES
        }
        options.update(kwargs)
        return super(CountryField, self).__init__(*args, **options)


# South introspection rules for custom fields
from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ['^trephub\.base\.models\.CountryField'])


class Sponsor(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(default='', unique=True)
    description = models.TextField()

    def _logo_path(self, filename):
        root, ext = os.path.splitext(filename)
        return 'sponsors/{0}{1}'.format(slugify(self.name), ext)
    logo = models.ImageField(upload_to=_logo_path)

    def get_absolute_url(self):
        return '#'.join((reverse('base.sponsors'), self.slug))

    def __unicode__(self):
        return u'<Sponsor `{0}`>'.format(self.name)
