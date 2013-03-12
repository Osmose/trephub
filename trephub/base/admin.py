from django.contrib import admin

from trephub.base import models


class SponsorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(models.Sponsor, SponsorAdmin)
