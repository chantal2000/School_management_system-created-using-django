
"""
Django settings for school_system project.

Generated by 'django-admin startproject' using Django 3.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
import django_heroku
import dj_database_url
from pathlib import Path


from django.conf.global_settings import MEDIA_ROOT, MEDIA_URL

BASE_DIR = Path(__file__).resolve().parent
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/
SECRET_KEY = 'django-insecure-2mkxz7y8kry+6dd*y=7nk*i(d(dao1wewml32^g&t-4bhsrw=*'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG =True
ALLOWED_HOSTS = []
STATIC_URL = '/1static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), ) 
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL = '/media/' 
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
LOGIN_REDIRECT_URL = '/'
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'student',
    'phonenumber_field',
    'bootstrap4',
    'rest_framework',
    'languages',
    'api',
    # 'world_languages',
    'django_countries',
    'trainer',
    'course',
    'calendarr',
    'core',
    # 'django.contrib.django_counties',

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

ROOT_URLCONF = 'school_system.urls'
MEDIA_URL='/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'student', 'templates', 'student'),
            os.path.join(BASE_DIR, 'course', 'templates', 'course'),
            os.path.join(BASE_DIR, 'trainer', 'templates', 'trainer'),
            os.path.join(BASE_DIR, 'calendarr', 'templates', 'calendarr'),
        ],
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

WSGI_APPLICATION = 'school_system.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#data
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'chantaldb',
        'USER': 'chantal',
        'PASSWORD': 'namuhoranye2000',
        'HOST': 'localhost',
        'PORT': '',
    }
}



db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)

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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'media')
STATICFILES_DIRS=[os.path.join(BASE_DIR,'statics')]
 

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
django_heroku.settings(locals())
