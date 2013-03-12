from django.contrib import admin

from trephub.events import models


class PhotoInline(admin.TabularInline):
    model = models.Photo
    fields = ('image',)
    extra = 1


class EventFileInline(admin.TabularInline):
    model = models.EventFile
    fields = ('name', 'file')
    extra = 1


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'attendance', 'location', 'created', 'updated')
    list_filter = ('location',)
    search_fields = ('name', 'location')

    readonly_fields = ('created', 'updated')
    prepopulated_fields = {'slug': ('name',)}
    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'created', 'updated'),
        }),
        ('Details', {
            'fields': ('start', 'end', 'location', 'attendance', 'summary',
                       'details'),
        }),
    )

    inlines = [PhotoInline, EventFileInline]
admin.site.register(models.Event, EventAdmin)


class LocationAdmin(admin.ModelAdmin):
    pass
admin.site.register(models.Location, LocationAdmin)
