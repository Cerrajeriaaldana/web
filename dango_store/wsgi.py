"""
WSGI config for dango_store project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
import sys

# Agrega tu directorio aquí
sys.path.append(0,'')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dango_store.settings')

application = get_wsgi_application()