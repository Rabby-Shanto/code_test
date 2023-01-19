import os
import sys

from .base import *

DEBUG = True
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

INSTALLED_APPS += ['UserSubscription.Customer','UserSubscription.Company','UserSubscription.Payment','rest_framework']

ROOT_URLCONF = 'config.urls'

ALLOWED_HOSTS = ['*']
DEBUG = True

SECRET_KEY = 'django-insecure-%+v398#4o874532me9ydg(r!kl1#k=g!+8(5-x%t9r8b+j$$r9'