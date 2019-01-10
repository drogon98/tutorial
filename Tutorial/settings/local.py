import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ctnwo4^lu@p*@=#rhs=g*zdq-xx23+#%!s#yx76iu&9o-e83vf'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []# key in your domain name here when you turn DEBUG off ie DEBUG=false

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',# from django.contrib import admin
    'django.contrib.auth', # from django.contrib import auth
    'django.contrib.contenttypes',# from django.contrib import contenttypes
    'django.contrib.sessions', # from django.contrib import sessions
    'django.contrib.messages', # from django.contrib import messages
    'django.contrib.staticfiles', # from django import staticfiles
    'accounts',
    'posts',

]
# each middleware performs a specific function
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware', # this middleware is required by django so u can exclude the others
    # at will
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',# associates users with requests using sessions
    # this miidleware associates a logged in user with the request.user attribute to every Htttprequest obj
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'Tutorial.middleware.LoginRequiredMiddleware',
]

ROOT_URLCONF = 'Tutorial.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'Tutorial.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
# handling staticfiles
STATICFILES_DIRS=[
        os.path.join(BASE_DIR,'static'),
        ]

MEDIA_URL='/media/'

MEDIA_ROOT=os.path.join(BASE_DIR,'Tutorial/media')


LOGIN_REDIRECT_URL="posts:home"

LOGIN_URL='/accounts/login/'
# email handling in debug mode

#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025

LOGIN_EXEMPT_URLS=(
     'accounts/register/',
     'accounts/password-reset/',
     'accounts/password-reset/done/',
     'accounts/password-reset-confirm/<uidb64>/<token>/',
     'accounts/password-reset-complete/',
     )
