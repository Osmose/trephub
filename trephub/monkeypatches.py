import jinja2


def patch():
    # Patch Markup to support jinja2 templates.
    from markupfield.fields import Markup

    def markup_unicode(self):
        return jinja2.Markup(self.rendered)
    Markup.__unicode__ = markup_unicode
