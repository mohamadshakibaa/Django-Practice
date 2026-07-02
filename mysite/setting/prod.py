from mysite.settings import *
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-(oe+=69yz%oj5%2)a)(cuc&7rr%%hxf#1*w0l6c_99n)jv#)nb"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []

# INSTALLED_APPS = []

# sites framework
SITE_ID = 2


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# STATIC_ROOT = BASE_DIR / "static"
STATICFILES_DIRS = [BASE_DIR / "statics"]
MEDIA_ROOT = BASE_DIR / "media"


# CSRF_COOKIE_SECURE = True