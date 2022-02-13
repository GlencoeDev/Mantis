"""

Glencoe Software: Mantis - Managment System
By: Glencoe Software Dev <http://glencoesoftware.ca>
Copyright (c) 2022, Glencoe Software Canada. All rights reserved.

"""


from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
# Override the default settings for the development environment

DEBUG = False

ADMIN_ENABLED = False

DATABASES = {"default": {"ENGINE": "djongo", "NAME": "mantis"}}
