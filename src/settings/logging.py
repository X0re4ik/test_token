import sys

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': "[%(levelname)4.4s %(asctime)s %(module)s:%(lineno)d] "
            "%(message)s",
            'datefmt': "%Y-%m-%d+%H:%M:%S",
        },
    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
            'stream': sys.stderr,
        },
        'rotating_to_file': {
            'level': 'DEBUG',
            'class': "logging.handlers.RotatingFileHandler",
            'formatter': 'standard',
            "filename": "app.log",
            "maxBytes": 10000,
            "backupCount": 10,
        },
    },
    'loggers': {
        '': {
            'handlers': ['default', 'rotating_to_file'],
            'level': 'INFO',
            'propagate': True
        }
    }
}