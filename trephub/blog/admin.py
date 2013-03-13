from django.contrib import admin

from trephub.blog import models


class BlogEntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'is_public', 'created', 'published')
    list_filter = ('author', 'is_public', 'published')
    search_fields = ('title', 'author__username', 'author__first_name',
                     'author__last_name', 'content')

    readonly_fields = ('author', 'created', 'updated', 'published')
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'is_public',),
        }),
        ('Metadata', {
            'fields': ('author', 'created', 'updated', 'published'),
        }),
        ('Post', {
            'fields': ('summary', 'content'),
        }),
    )

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.save()
admin.site.register(models.BlogEntry, BlogEntryAdmin)
