import os

from .base import *

DEBUG = False

ALLOWED_HOSTS = ['itnsa.cn', 'www.itnsa.cn', '192.168.238.101']

with open('/etc/django/secret_key.txt', 'r') as f:
    SECRET_KEY = f.read().strip()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': '/etc/django/my.cnf',
        },
    }
}

STATIC_ROOT = '/var/www/itnsa/static'
MEDIA_ROOT = '/var/www/itnsa/media'