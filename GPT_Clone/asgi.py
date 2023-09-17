"""
ASGI config for GPT_Clone project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this gpt, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GPT_Clone.settings')

application = get_asgi_application()
