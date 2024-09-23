from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'cizu0lzvi#y+(+^72jdam^tcr#uw!&!gu#ydfnjf@z^+)5h)1e'

DEBUG = True

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'students.apps.StudentsConfig',
    'base.apps.BaseConfig',
    'assignments.apps.AssignmentsConfig',
    'exams.apps.ExamsConfig',
    'feedbacks.apps.FeedbacksConfig',
    'library.apps.LibraryConfig',
    'classes.apps.ClassesConfig',
    'profiles.apps.ProfilesConfig',
    'timetables.apps.TimetablesConfig',
    'informations.apps.InformationsConfig',
    "rest_framework",
    'django_celery_results',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    # Add providers for social logins (e.g., Google)
    'allauth.socialaccount.providers.google',
    # 'django-celery-beat'
    ]

INSTALLED_APPS += ('django_celery_beat',)
AUTH_USER_MODEL = 'students.CustomUser'
AUTH_USER_MODEL = 'students.CustomUser'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
SITE_ID = 1
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
        'allauth.account.auth_backends.AuthenticationBackend',

)
# Redirect users after login
LOGIN_REDIRECT_URL = '/'

# Email verification mandatory
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

# Require email and not username for login
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ROOT_URLCONF = 'attendance.urls'

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
    }
}
ACCOUNT_FORMS = {
    'signup': 'your_app_name.forms.CustomSignupForm',
}
LOGIN_REDIRECT_URL = '/dashboard/'

# Email verification requirement
ACCOUNT_EMAIL_VERIFICATION = 'optional'

# Require email during signup
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False

# Unique email addresses for users
ACCOUNT_UNIQUE_EMAIL = True
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates'
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

WSGI_APPLICATION = 'attendance.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'attendance',
        'USER': 'root',
        'PASSWORD': 'vijay',
        'HOST': 'localhost',   
        'PORT': '3306',  
    }
}

# Add this line to enable PyMySQL as the MySQL client:
import pymysql
pymysql.install_as_MySQLdb()

# DEBUG=True
# DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]

# # MySQL settings
# MYSQL_ROOT_PASSWORD=your-mysql-root-password
# MYSQL_DATABASE=
# MYSQL_USER="root"
# MYSQL_PASSWORD="vijay"

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True
SITE_ID = 1


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

import os
STATIC_URL = 'static/'
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),  # For development
]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# settings.py
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'vijaygholve77v@gmail.com'
EMAIL_HOST_PASSWORD = 'uoyn xeho visj fblr'  



import ssl

CELERY_BROKER_URL = 'redis://127.0.0.1:6379/0'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TIMEZONE = "Asia/Kolkata"
CELERY_ENABLE_UTC = False
CELERY_RESULT_BACKEND='django-db'
# Retain existing behavior for retrying connections on startup
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True

CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"

# Only include SSL configuration if using SSL
# CELERY_BROKER_USE_SSL = {
#     'ssl_cert_reqs': ssl.CERT_NONE  # Adjust based on your security requirements
# }

timezone = 'Asia/Kolkata'
accept_content = ['json']
result_backend = 'redis://127.0.0.1:6379/0'
result_serializer = 'json'
task_serializer = 'json' 
