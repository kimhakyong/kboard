"""
Django settings for kboard project.

Generated by 'django-admin startproject' using Django 1.10.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
from django.core.mail import send_mail

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'fbk#a_$7&@566onvmd1xfxyszz)npb+d5gq#y9q(n0wg_k)v0x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'board',
    'django_summernote',
    'djangobower',
    'pipeline'
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'kboard.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,  'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'kboard.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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

# Bower settings
BOWER_INSTALLED_APPS = [
    'jquery#^2.2',
    'react',
    'react-bootstrap',
    'bootswatch-dist#simplex'
]
BOWER_COMPONENTS_ROOT = os.path.join(BASE_DIR, '../')

# Summernote settings

SUMMERNOTE_CONFIG = {}

# pipeline settings
PIPELINE = {
    'PIPELINE_ENABLED': False,
    'COMPILERS': {
        'libsasscompiler.LibSassCompiler',
    },
    'JAVASCRIPT': {
        'main': {
            'source_filenames': [
              'js/*.js'
            ],
            'output_filename': 'js/vendor.js'
        },
    },
    'STYLESHEETS': {
        'main': {
            'source_filenames': [
              'style/*.scss'
            ],
            'output_filename': 'style/main.css'
        },
    },
}

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '../static')

STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BOWER_COMPONENTS_ROOT, 'bower_components'),
]

MEDIA_URL = '/media/'


# Registration
# https://django-registration.readthedocs.io/en/2.1.2/index.html

ACCOUNT_ACTIVATION_DAYS = 7


# Email Activation

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'chsun0303@gmail.com'
EMAIL_HOST_PASSWORD = os.environ.get('KBOARD_PASSWORD')
SERVER_EMAIL = 'chsun0303@gmail.com'
DEFAULT_FROM_MAIL = 'KBoard_Developer'


# When Login success, go to main page.

LOGIN_REDIRECT_URL = "/"