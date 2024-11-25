import environ

from .base import *

env = environ.Env()
environ.Env.read_env()

SECRET_KEY = env.str("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DEBUG")

ALLOWED_HOSTS = ["*"]

THIRD_PARTY_APP = [
    
]

INSTALLED_APPS = INSTALLED_APPS + THIRD_PARTY_APP

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}