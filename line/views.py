import sys
import base64
import hashlib
import hmac
import json
import logging

from django.http import (
    HttpResponse,
)
from django.views.decorators.csrf import csrf_exempt
from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError

from lugia.settings import CHANNEL_SECRET, CHANNEL_ACCESS_TOKEN


stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.INFO)
handlers = [stdout_handler]
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s; %(asctime)s; %(module)s:%(funcName)s:%(lineno)d; %(message)s",
    handlers=handlers,
)

logger = logging.getLogger(__name__)


@csrf_exempt
def line_webhook_view(
    request,
):
    if not verify(request):
        return HttpResponse("This request isn't from Line!")

    try:
        reply(request)
        return HttpResponse("reply succeeded!")

    except Exception as e:
        logger.error(e)
        return HttpResponse("reply failed!")


def verify(request):
    body = request.body
    hash = hmac.new(CHANNEL_SECRET.encode("utf-8"), body, hashlib.sha256).digest()
    signature = base64.b64encode(hash).decode("utf-8")

    return request.headers.get("x-line-signature") == signature


def reply(request):
    events = json.loads(request.body)
    events = events.get("events", [])

    for event in events:
        reply_token = event.get("replyToken")

        if not reply_token or event.get("type") != "message":
            continue

        line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
        line_bot_api.reply_message(reply_token, TextSendMessage(text="Hello World!"))
