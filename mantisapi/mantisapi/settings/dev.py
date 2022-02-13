"""

Glencoe Software: Mantis - Managment System
By: Glencoe Software Dev <http://glencoesoftware.ca>
Copyright (c) 2022, Glencoe Software Canada. All rights reserved.

"""

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
# Override the default settings for the development environment

DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}
