import dj_database_url
from decouple import config

from .base import *

DEBUG = False

SECRET_KEY = config('SECRET_KEY')

MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware',]

DATABASES = {
	'default': dj_database_url.config(
		default=config('DATABASE_URL')
	)
}

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'