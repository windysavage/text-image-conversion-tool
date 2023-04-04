from django.urls import (
    path,
)

from .views import (
    webhook_view,
)

urlpatterns = [
    path(
        "messenger_webhook",
        webhook_view,
        name="messenger_webhook",
    ),
]
