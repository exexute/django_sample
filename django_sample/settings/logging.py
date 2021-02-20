from django.utils.log import DEFAULT_LOGGING

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'django.server': DEFAULT_LOGGING['formatters']['django.server']
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/sample_log.log',
            'backupCount': 5,
            'maxBytes': 128,
        },
        'django.server': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/access.log',
            'backupCount': 5,
            'maxBytes': 1024 * 5,
            'formatter': 'django.server',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'WARNING',
    },
    'loggers': {
        'sample_log': {
            'handlers': ['file'],
            'level': 'INFO',
        },
        'django.server': {
            'handlers': ['django.server'],
            'level': 'INFO',
            'propagate': False,
        },
        # 'django': {
        #     'handlers': ['console', 'django.server'],
        #     'level': 'DEBUG',
        #     'propagate': False,
        # },
    }
}
