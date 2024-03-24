"""
Django settings for django_project project.

Generated by 'django-admin startproject' using Django 2.2.12.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import netifaces

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '467e513b5923aa93b0b2f390135d2b61'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Find out what the IP addresses are at run time
# This is necessary because otherwise Gunicorn will reject the connections
def ip_addresses():
    ip_list = []
    for interface in netifaces.interfaces():
        addrs = netifaces.ifaddresses(interface)
        for x in (netifaces.AF_INET, netifaces.AF_INET6):
            if x in addrs:
                ip_list.append(addrs[x][0]['addr'])
    return ip_list

ALLOWED_HOSTS = ['nadlan-abroad.world', 'localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_ckeditor_5',
    'django_cleanup.apps.CleanupConfig',
    'corsheaders',
    'main.apps.MainConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_project.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'django_project.wsgi.application'

CORS_ALLOW_ALL_ORIGINS = True

# CORS_ORIGIN_WHITELIST =[]

CSRF_TRUSTED_ORIGINS = ['https://nadlan-abroad.world', 'http://nadlan-abroad.world', 'http://localhost:3000', 'http://127.0.0.1:3000']
CSRF_COOKIE_SECURE = True

CSRF_COOKIE_SAMESITE = None

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME':  '/workspaces/nadlan-world-back/django_project/sql_django.sqlite3',

    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        # 'rest_framework.renderers.JSONRenderer', 
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
    # 'rest_framework.authentication.SessionAuthentication',
    'rest_framework.authentication.BasicAuthentication',
]
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

MEDIA_URL = '/image/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'image/')


customColorPalette = [
    {"color": "hsl(4, 90%, 58%)", "label": "Red"},
    {"color": "hsl(340, 82%, 52%)", "label": "Pink"},
    {"color": "hsl(291, 64%, 42%)", "label": "Purple"},
    {"color": "hsl(262, 52%, 47%)", "label": "Deep Purple"},
    {"color": "hsl(231, 48%, 48%)", "label": "Indigo"},
    {"color": "hsl(207, 90%, 54%)", "label": "Blue"},
]
CKEDITOR_5_CONFIGS = {
    "default": {
        'width': '100%',
        "language":{
            "ui": "ru",
            # "content": "ru"
        },
        'toolbar': ['Undo', 'Redo', 
                    '|', 'heading', 
                    '|', 'bold', 'italic',  'underline', 'strikethrough',
                    '|', 'alignment', 
                    '|', 'link', 'indent', 'outdent',  
                    '|', 'fontFamily', 'fontSize', 'fontColor', 'fontBackgroundColor',
                    '|','bulletedList', 'numberedList', 'todoList', 
                    '|', 'blockQuote', 'subscript', 'superscript', 'highlight', 
                    '|', 'removeFormat', ],
    },
    'title':{
        'width': '100%',
        "language":{
            "ui": "ru",
            # "content": "he"
        },
        'toolbar': ['Undo', 'Redo', 
                    '|', 'heading', 
                    '|', 'bold', 'italic',  'underline', 'strikethrough',
                    '|', 'alignment', 
                    '|', 'link', 'indent', 'outdent',  
                    '|', 'fontFamily', 'fontSize', 'fontColor', 'fontBackgroundColor',
                    '|', 'blockQuote', 'subscript', 'superscript', 'highlight', 
                    '|', 'removeFormat', ],
    },

}