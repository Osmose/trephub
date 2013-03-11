# This is your project's main settings file that can be committed to your
# repo. If you need to override a setting locally, use settings_local.py

from funfactory.settings_base import *

# Defines the views served for root URLs.
ROOT_URLCONF = 'trephub.urls'

INSTALLED_APPS = list(INSTALLED_APPS) + [
    'trephub.base',
    'trephub.events',

    'jingo_minify',
    'south',

    'django.contrib.admin',
]

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'session_csrf.CsrfMiddleware',  # Must be after auth middleware.
    'django.contrib.messages.middleware.MessageMiddleware',
    'commonware.middleware.FrameOptionsHeader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'session_csrf.context_processor',
    'django.contrib.messages.context_processors.messages',
    'funfactory.context_processors.globals',
)

# Because Jinja2 is the default template loader, add any non-Jinja templated
# apps here:
JINGO_EXCLUDE_APPS = [
    'admin',
    'registration',
]

SITE_URL = 'http://localhost:8000'

# Should robots.txt deny everything or disallow a calculated list of URLs we
# don't want to be crawled?  Default is false, disallow everything.
# Also see http://www.google.com/support/webmasters/bin/answer.py?answer=93710
ENGAGE_ROBOTS = False

# Always generate a CSRF token for anonymous users.
ANON_ALWAYS = True

# Force jingo-minify to use static paths.
JINGO_MINIFY_USE_STATIC = True

# Meetup Group Info
MEETUP_GROUP_URLNAME = 'Coders-Hackers-Founders'

# Static asset bundles
MINIFY_BUNDLES = {
    'css': {
        'base': (
            'css/bootstrap.css',
            'css/base.css',
        ),
        'home': (
            'css/home.css',
        ),
    },
    'js': {
        'base': (
            'js/bootstrap.js',
        ),
    },
}
