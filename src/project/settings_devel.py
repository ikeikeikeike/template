from .settings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# DATABASES = {
    # 'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': '/dev/shm/myapp.db',
    # }
# }

# database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'template',                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

MYAPP_USERNAME = 'foo@domain'
MYAPP_PASSWORD = '12345678'
