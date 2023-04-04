from django.http import (
    HttpResponse,
)

from lugia.settings import FACEBOOK_WEBHOOK_TOKEN


def webhook_view(
    request,
):
    query_dict = request.GET
    verified_result = verify(query_dict)
    return HttpResponse(f"{verified_result}")


def verify(query_dict):
    mode = query_dict.get("hub.mode")
    token = query_dict.get("hub.verify_token")
    challenge = query_dict.get("hub.challenge")

    if token != FACEBOOK_WEBHOOK_TOKEN:
        return

    return challenge
