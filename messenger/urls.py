from django.urls import (
    path,
)

from .views import (
    messenger_webhook_view,
)

urlpatterns = [
    path(
        "messenger_webhook",
        messenger_webhook_view,
        name="messenger_webhook",
    ),
]
