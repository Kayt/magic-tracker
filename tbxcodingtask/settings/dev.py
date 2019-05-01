from .base import *  # noqa
DEBUG = True
SECRET_KEY = 'foo'
ALLOWED_HOSTS = ['*']
INTERNAL_IPS = ('127.0.0.1', '10.0.2.2')
BASE_URL = 'http://localhost:8000'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
AUTH_PASSWORD_VALIDATORS = []
INSTALLED_APPS += ['django_extensions']  # noqa
SECURE_SSL_REDIRECT = False
