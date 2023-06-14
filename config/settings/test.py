from .base import *  # noqa


DEBUG = False
PASSWORD_HASHERS = ['settings.contrib.auth.hashers.MD5PasswordHasher']

CELERY_BROKER_BACKEND = "memory"
CELERY_TASK_ALWAYS_EAGER = True
CELERY_TASK_EAGER_PROPAGATES = True

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
    }
}

DATABASES = {
        "default": {
        "ENGINE": "settings.db.backends.sqlite3",
        "NAME": "db.sqlite3",
        }
    }
