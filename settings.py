# Note: Set the following env variables:
# MAINTDX_SECRET_KEY
# MAINTDX_DB_USER
# MAINTDX_DB_PASS
# MAINTDX_DB_NAME

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = os.environ.get("MAINTDX_SECRET_KEY")

DEBUG = True
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"
ALLOWED_HOSTS = []

CORS_ORIGIN_ALLOW_ALL = True

GRAPHENE = {"SCHEMA": "maintdx.schema.schema"}

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.postgres",
    "django_filters",
    "corsheaders",
    "graphene_django",
    "maintdx.assets",
    "maintdx.parts.apps.PartsConfig",
    "maintdx.vendors",
    "maintdx.workorders",
    "maintdx.users",
    "maintdx.dashboard",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

DEV_HOST = "http://127.0.0.1:8000"
ROOT_URLCONF = "maintdx.urls"
MEDIA_ROOT = "/home/derek/code/maintdx/maintdx/media/"
MEDIA_URL = "/media/"
ABSOLUTE_MEDIA_URL = "%s%s" % (DEV_HOST, MEDIA_URL)
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "maintdx/templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "maintdx.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("MAINTDX_DB_NAME"),
        "USER": os.environ.get("MAINTDX_DB_USER"),
        "PASSWORD": os.environ.get("MAINTDX_DB_PASS"),
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = "/static/"
# STATIC_ROOT = os.path.join(BASE_DIR, "maintdx/static")
STATICFILES_DIRS = [os.path.join(BASE_DIR, "maintdx/static")]
