import os
from .base import *

DEBUG = False
# Use the real domain of Property Bazaar here
ALLOWED_HOSTS = ['api.propertybazaar.com', 'www.propertybazaar.com']

# In Prod, you likely use PostgreSQL
import dj_database_url
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL')
    )
}

# Strict Security for Prod
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
