from local_settings import *

# STANDARD DJANGO STUFF
TEMPLATE_DEBUG = False
WSGI_APPLICATION = 'www.wsgi.prod_application'

# !!!! SECURITY SECTION
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# !!!! END SECURITY SECTION

# END STANDARD DJANGO STUFF


# STATIC FILE CONFIGURATION
# From https://devcenter.heroku.com/articles/django-assets
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
# END STATIC FILE CONFIGURATION
