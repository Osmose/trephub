import urllib

from django.contrib.auth.models import User
from django.template.defaultfilters import date
from django.utils.hashcompat import md5_constructor

import jinja2
from jingo import register


register.filter(date)


@register.function
def gravatar_url(arg, size=80):
    if isinstance(arg, User):
        email = arg.email
    else:  # Treat as email
        email = arg

    url = 'https://secure.gravatar.com/avatar/{0}?{1}'.format(
        md5_constructor(email.lower()).hexdigest(),
        urllib.urlencode({'s': str(size), 'default': 'mm'})
    )

    return url


@register.function
def gravatar_img(arg, size=80):
    return jinja2.Markup('<img src="%s">' % gravatar_url(arg, size=size))
