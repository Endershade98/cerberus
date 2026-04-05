# config/settings/test.py
from .settings import *

# usa SQLite in-memory per i test
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

# disabilita cache complessa
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache"
    }
}

# riduci logging o altre configurazioni per test
DEBUG = False