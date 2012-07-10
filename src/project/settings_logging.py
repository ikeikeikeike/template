import os

PROJECT_ROOT = os.getenv('PROJECT_ROOT') or os.path.join(os.path.dirname(__file__), '../..')
LOGDIR = os.path.abspath(os.path.join(PROJECT_ROOT, "log"))

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    "formatters": {
        "verbose": {
            "format": "%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]"
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        "console":{
            "level":"DEBUG",
            "class":"logging.StreamHandler",
            "formatter": "verbose",
        },
        "debug":{
            "level":"DEBUG",
            "class":"logging.handlers.TimedRotatingFileHandler",
            "formatter": "verbose",
            "filename": os.path.join(LOGDIR, "appserver_debug.log"),
            "when": "H",
        },
        "appinfo":{
            "level":"INFO",
            "class":"logging.handlers.TimedRotatingFileHandler",
            "formatter": "verbose",
            "filename": os.path.join(LOGDIR, "appserver_out.log"),
        },
#        "fluentinfo":{
#            "level":"INFO",
#            "class":"fluent.handler.FluentHandler",
#            "formatter": "verbose",
#            "tag":"app.info",
#            "host":"localhost",
#            "port":24224,
#            # "timeout":3.0,
#            # "verbose": False
#        },
#        "fluentdebug":{
#            "level":"DEBUG",
#            "class":"fluent.handler.FluentHandler",
#            "formatter": "verbose",
#            "tag":"app.debug",
#            "host":"localhost",
#            "port":24224,
#            # "timeout":3.0,
#            "verbose": True
#        },
#        'sentry': {
#            'level': 'ERROR',
#            'class': 'raven.contrib.django.handlers.SentryHandler',
#        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
