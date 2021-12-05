"""
ASGI config for asyncPractice project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from channels.security.websocket import AllowedHostsOriginValidator
from channels.auth import AuthMiddlewareStack
from core.consumer import (
    WsConsumer,
)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'asyncPractice.settings')

urlpatterns = [
    path('counter/', WsConsumer.as_asgi()),
]


application = ProtocolTypeRouter({
    # Django's ASGI application to handle traditional HTTP requests
    "http": get_asgi_application(),

    # Django's ASGI application to handle websockets
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(urlpatterns)
        )
    )

})

'''
ws://127.0.0.1:8000/
AllowedHostsOriginValidator = allow host names given in the settings.py
AuthMiddlewareStack = enable login session to be stored, to use scope['user']
'''
