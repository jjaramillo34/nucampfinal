"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 4.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import django_heroku
import dj_database_url
#import environ
import os
from pathlib import Path
from decouple import config
from django.utils.translation import gettext_lazy as _


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = config('DEBUG')
DEBUG = False
#ALLOWED_HOSTS = config('ALLOWED_HOSTS')
#ALLOWED_HOSTS = ['*']
ALLOWED_HOSTS = ['ec2-34-238-116-99.compute-1.amazonaws.com', '0.0.0.0', '127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    
    #apps
    'home',
    'testimonials',
    'contact',
    'projects',
    'courses',
    'comment',
    'blog',
    'resume',
    'services',
    
    #third party apps
    'ckeditor',
    'ckeditor_uploader',
    #"crispy_forms",
    #"crispy_bootstrap5",
    "widget_tweaks",
    #'bootstrap_modal_forms',
    #'social_django',
    'rosetta',  # NEW
    'parler',  # NEW
    #'hitcount',
    'django_json_widget',
    'captcha',
    'tinymce',
    #'highlightjs',
    
    #"debug_toolbar",
    #'snowpenguin.django.recaptcha3',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware', # new
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #"debug_toolbar.middleware.DebugToolbarMiddleware",
]

HIGHLIGHTJS = {
    # The URL to the jQuery JavaScript file
    'jquery_url': '//code.jquery.com/jquery.min.js',
    # The highlight.js base URL
    'base_url': '//cdnjs.cloudflare.com/ajax/libs/highlight.js/8.3/highlight.min.js',
    # The complete URL to the highlight.js CSS file
    'css_url': '//cdnjs.cloudflare.com/ajax/libs/highlight.js/8.3/styles/{0}.min.css',
    # Include jQuery with highlight.js JavaScript (affects django-highlightjs template tags)
    'include_jquery': False,
    # The default used style.
    'style': 'monokai_sublime',
    }


#INTERNAL_IPS = [
#    # ...
#    "127.0.0.1",
#    # ...
#]

MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#    }
#}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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

AUTHENTICATION_BACKENDS = (
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.google.GoogleOAuth2',

    'django.contrib.auth.backends.ModelBackend',
)

LANGUAGE_CODE = 'en'

TIME_ZONE = 'US/Eastern'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = (
    ('en', _('English')),
    ('fr', _('French')),
    ('es', _('Spanish')),
    ('pt-br', _('Brazilian Portuguese')),
)

LOCALE_PATHS = [
    BASE_DIR / 'locale/',
]

PARLER_LANGUAGES = {
    1: (
        {'code': 'en',}, # English
        {'code': 'fr',}, # French
        {'code': 'es',}, # Spanish
        {'code': 'pt-br',}, # Brazilian Portuguese
    ),
    'default': {
        'fallbacks': ['en'],
        'hide_untranslated': False,
    }
}

SILENCED_SYSTEM_CHECKS = ['captcha.recaptcha_test_key_error']

RECAPTCHA_REQUIRED_SCORE = 0.85

RECAPTCHA_DEFAULT_ACTION = 'generic'
RECAPTCHA_SCORE_THRESHOLD = 0.5
#RECAPTCHA_LANGUAGE = 'en' # for auto detection language, remove this from your settings
# If you require reCaptcha to be loaded from somewhere other than https://google.com
# (e.g. to bypass firewall restrictions), you can specify what proxy to use.
# RECAPTCHA_FRONTEND_PROXY_HOST = 'https://recaptcha.net'

#development v2
RECAPTCHA_PUBLIC_KEY = config('RECAPTCHA_PUBLIC_KEY')
RECAPTCHA_PRIVATE_KEY = config('RECAPTCHA_PRIVATE_KEY')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Extra places for collectstatic to find static files.
#STATICFILES_DIRS = (os.path.join(BASE_DIR, 'staticfiles'),)

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/user/login/'

# social auth configs for github
SOCIAL_AUTH_GITHUB_KEY = str(os.getenv('GITHUB_KEY'))
SOCIAL_AUTH_GITHUB_SECRET = str(os.getenv('GITHUB_SECRET'))

# social auth configs for google
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = str(os.getenv('GOOGLE_KEY'))
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = str(os.getenv('GOOGLE_SECRET'))

# email configs
SENDGRID_API_KEY = config('SENDGRID_API_KEY')

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey' # this is exactly the value 'apikey'
EMAIL_HOST_PASSWORD = SENDGRID_API_KEY
EMAIL_PORT = 587
EMAIL_USE_TLS = True

SESSION_COOKIE_AGE = 60 * 60 * 24 * 30

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CKEDITOR_UPLOAD_PATH = 'uploads/'

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 1200,
        'width': 1000,
        'image2_alignClasses': [ 'image-left', 'image-center', 'image-right' ],
        'image2_captionedClass': 'image=captioned',
        'codeSnippet_theme': 'pojoaque',
        'language_list': [ 'en:English', 'pt:Portuguese', 'fr:French', 'es:Spanish'],
        'extraPlugins': ','.join(
            [
               'html5audio',
               'codesnippet',
               'N1ED-editor',
            ]
        ),  
    },
}

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

# Heroku configs
django_heroku.settings(locals())
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

# Cloudinary stuff
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': config('CLOUD_NAME', default=""),
    'API_KEY': config('API_KEY', default=""),
    'API_SECRET': config('API_SECRET', default=""),
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

SESSION_COOKIE_AGE = 36000000

TINYMCE_JS_URL = '"https://cdn.tiny.cloud/1/t2hig0olqqh0rbzmri0waez8fx86sxj1typhf2pus8uqzara/tinymce/6/tinymce.min.js"'
TINYMCE_COMPRESSOR = False

TINYMCE_DEFAULT_CONFIG = {
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 20,
    'selector': 'textarea',
    'theme': 'silver',
    "height": 500,
    'plugins': '''
            textcolor save link image media preview codesample contextmenu
            table code lists fullscreen  insertdatetime  nonbreaking
            contextmenu directionality searchreplace wordcount visualblocks
            visualchars code fullscreen autolink lists  charmap print  hr
            anchor pagebreak
            ''',
    'toolbar1': '''
            fullscreen preview bold italic underline | fontselect,
            fontsizeselect  | forecolor backcolor | alignleft alignright |
            aligncenter alignjustify | indent outdent | bullist numlist table |
            | link image media | codesample |
            ''',
    'toolbar2': '''
            visualblocks visualchars |
            charmap hr pagebreak nonbreaking anchor |  code |
            ''',
    'contextmenu': 'formats | link image',
    'menubar': True,
    'statusbar': True,
}