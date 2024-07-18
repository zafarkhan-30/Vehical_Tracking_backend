

import os
import django
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'VehicalTracking.settings')

django.setup()

from vehicle.routing import websocket_urlpatterns
from .middleware import TokenAuthMiddleware
from channels.security.websocket import AllowedHostsOriginValidator


asgi_application = get_asgi_application()

application = ProtocolTypeRouter({
    "http": asgi_application,
    "websocket":AllowedHostsOriginValidator(
            TokenAuthMiddleware(
        URLRouter(
            websocket_urlpatterns
        )
    ),
    )
})
