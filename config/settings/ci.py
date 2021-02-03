from .base import *


# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


DATABASES = {
	'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': root('barber/db.sqlite3'),
    }
}