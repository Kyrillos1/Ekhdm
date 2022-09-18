"""
WSGI config for ekhdm demomethod.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangodemomethod.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ekhdm.settings')

application = get_wsgi_application()
