"""
ASGI config for ekhdm demomethod.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangodemomethod.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ekhdm.settings')

application = get_asgi_application()
