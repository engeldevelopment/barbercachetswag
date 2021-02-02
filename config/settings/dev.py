from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z2as7)^hfq18l9dyvfj_1hn5^fj490317gba=95*gco4w6*geo'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


DATABASES = {
	'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': root('barber/db.sqlite3'),
    }
}
