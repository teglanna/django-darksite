DEBUG = False

ALLOWED_HOSTS = ['18.216.94.1', 'teglanna.rocks', 'www.teglanna.rocks']

import json

SECRET_KEY = ''
AWS_SECRET_ACCESS_KEY = ''

with open('/opt/bitnami/apps/django/django_projects/keys.json') as data_file:
    data = json.load(data_file)
    SECRET_KEY = data['django_key']
    AWS_SECRET_ACCESS_KEY = data['aws_key']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'whereami',
    'storages',
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

ROOT_URLCONF = 'darksite.urls'

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

WSGI_APPLICATION = 'darksite.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'darksite',
        'USER': 'postgres',
        'PASSWORD': 'WWBLmT4qEEb7',
        'HOST': 'localhost',
        'PORT': '',
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Berlin'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# AWS S3 setup
AWS_STORAGE_BUCKET_NAME = 'django-teglanna-ec2cloud'
AWS_S3_REGION_NAME = 'eu-central-1'
AWS_ACCESS_KEY_ID = "AKIAIOX6CRRD2EEWNOJQ"

#custom domain with s3
#AWS_S3_CUSTOM_DOMAIN = "s3.{}.amazonaws.com/{}".format(AWS_S3_REGION_NAME, AWS_STORAGE_BUCKET_NAME)

#custom domain with CDN
AWS_S3_CUSTOM_DOMAIN = 'd3pyuqss8xuxgi.cloudfront.net'
STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'aws_storage_classes.StaticStorage'

MEDIAFILES_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 'aws_storage_classes.MediaStorage'

STATIC_URL = "https://%s/static/" % AWS_S3_CUSTOM_DOMAIN
STATIC_ROOT = '/opt/bitnami/apps/django/django_projects/Project/static/'

MEDIA_URL = "https://%s/media/" % AWS_S3_CUSTOM_DOMAIN
MEDIA_ROOT = '/opt/bitnami/apps/django/django_projects/Project/media/'

# SECURITY SETTINGS
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
