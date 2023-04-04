from django.urls import (
    path,
)

from .views import (
    line_webhook_view,
)

urlpatterns = [
    path(
        "line_webhook",
        line_webhook_view,
        name="line_webhook",
    ),
]
