import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
django_asgi_app = get_asgi_application()

from channels.routing import ProtocolTypeRouter, URLRouter
from django_channels_jwt_auth_middleware.auth import JWTAuthMiddlewareStack
from donations.ws_routes import websockets_urlpatterns as donations_ws_urlpatterns

application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        "websocket": JWTAuthMiddlewareStack(URLRouter(donations_ws_urlpatterns)),
    }
)
