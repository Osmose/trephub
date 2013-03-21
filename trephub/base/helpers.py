from django.template.defaultfilters import date

from jingo import register


register.filter(date)
