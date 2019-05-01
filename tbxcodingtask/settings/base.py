"""
Django settings for tbxcodingtask project.
"""
import os
import sys

import dj_database_url

env = os.environ.copy()

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)
DEBUG = False

if 'SECRET_KEY' in env:
    SECRET_KEY = env['SECRET_KEY']

if 'ALLOWED_HOSTS' in env:
    ALLOWED_HOSTS = env['ALLOWED_HOSTS'].split(',')

INSTALLED_APPS = [
    'tbxcodingtask.core',
    'tbxcodingtask.tracker',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',

    'crispy_forms',
    'crispy_forms_foundation',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'tbxcodingtask.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'builtins': [],
        },
    },
]

WSGI_APPLICATION = 'tbxcodingtask.wsgi.application'

DATABASES = {
    'default': dj_database_url.config(conn_max_age=600, default='postgres:///tbxcodingtask'),
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'database_cache',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-gb'
TIME_ZONE = 'Europe/London'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

WHITENOISE_ROOT = os.path.join(BASE_DIR, 'public'),

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, 'static'),
]

STATIC_ROOT = env.get('STATIC_DIR', os.path.join(BASE_DIR, 'static'))
STATIC_URL = env.get('STATIC_URL', '/static/')
MEDIA_ROOT = env.get('MEDIA_DIR', os.path.join(BASE_DIR, 'media'))
MEDIA_URL = env.get('MEDIA_URL', '/media/')

if 'EMAIL_HOST' in env:
    EMAIL_HOST = env['EMAIL_HOST']

if 'EMAIL_PORT' in env:
    try:
        EMAIL_PORT = int(env['EMAIL_PORT'])
    except ValueError:
        pass

if 'EMAIL_HOST_USER' in env:
    EMAIL_HOST_USER = env['EMAIL_HOST_USER']

if 'EMAIL_HOST_PASSWORD' in env:
    EMAIL_HOST_PASSWORD = env['EMAIL_HOST_PASSWORD']

if env.get('EMAIL_USE_TLS', 'false').lower().strip() == 'true':
    EMAIL_USE_TLS = True

if env.get('EMAIL_USE_SSL', 'false').lower().strip() == 'true':
    EMAIL_USE_SSL = True

if 'EMAIL_SUBJECT_PREFIX' in env:
    EMAIL_SUBJECT_PREFIX = env['EMAIL_SUBJECT_PREFIX']

if 'SERVER_EMAIL' in env:
    SERVER_EMAIL = DEFAULT_FROM_EMAIL = env['SERVER_EMAIL']

try:
    CACHE_CONTROL_S_MAXAGE = int(env.get('CACHE_CONTROL_S_MAXAGE', 600))
except ValueError:
    pass

CACHE_CONTROL_STALE_WHILE_REVALIDATE = int(
    env.get('CACHE_CONTROL_STALE_WHILE_REVALIDATE', 30)
)

if env.get('SECURE_SSL_REDIRECT', 'true').strip().lower() == 'true':
    SECURE_SSL_REDIRECT = True

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

if 'SECURE_HSTS_SECONDS' in env:
    SECURE_HSTS_SECONDS = int(env['SECURE_HSTS_SECONDS'])

if env.get('SECURE_BROWSER_XSS_FILTER', 'true').lower().strip() == 'true':
    SECURE_BROWSER_XSS_FILTER = True

if env.get('SECURE_CONTENT_TYPE_NOSNIFF', 'true').lower().strip() == 'true':
    SECURE_CONTENT_TYPE_NOSNIFF = True

if 'CSP_DEFAULT_SRC' in env:
    MIDDLEWARE.append('csp.middleware.CSPMiddleware')

    CSP_DEFAULT_SRC = env.get('CSP_DEFAULT_SRC').split(',')
    if 'CSP_SCRIPT_SRC' in env:
        CSP_SCRIPT_SRC = env.get('CSP_SCRIPT_SRC').split(',')
    if 'CSP_STYLE_SRC' in env:
        CSP_STYLE_SRC = env.get('CSP_STYLE_SRC').split(',')
    if 'CSP_IMG_SRC' in env:
        CSP_IMG_SRC = env.get('CSP_IMG_SRC').split(',')
    if 'CSP_CONNECT_SRC' in env:
        CSP_CONNECT_SRC = env.get('CSP_CONNECT_SRC').split(',')
    if 'CSP_FONT_SRC' in env:
        CSP_FONT_SRC = env.get('CSP_FONT_SRC').split(',')
    if 'CSP_BASE_URI' in env:
        CSP_BASE_URI = env.get('CSP_BASE_URI').split(',')
    if 'CSP_OBJECT_SRC' in env:
        CSP_OBJECT_SRC = env.get('CSP_OBJECT_SRC').split(',')

REFERRER_POLICY = env.get('SECURE_REFERRER_POLICY',
                          'no-referrer-when-downgrade').strip()

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
