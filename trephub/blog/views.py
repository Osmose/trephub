from django.views.generic import DetailView, ListView

from trephub.blog.models import BlogEntry


class BlogEntryList(ListView):
    queryset = BlogEntry.objects.filter(is_public=True).order_by('-published')
    paginate_by = 5
    context_object_name = 'entries'
    template_name = 'blog/list.html'


class BlogEntryDetail(DetailView):
    queryset = BlogEntry.objects.filter(is_public=True)
    context_object_name = 'entry'
    template_name = 'blog/details.html'

    def get_context_data(self, **kwargs):
        context = super(BlogEntryDetail, self).get_context_data(**kwargs)
        context['older_entry'] = self.object.get_older(is_public=True)
        context['newer_entry'] = self.object.get_newer(is_public=True)
        return context
