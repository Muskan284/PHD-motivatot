import os
import logging
import requests

log = logging.getLogger(__name__)

_INSTANCE_ID = os.getenv("GREEN_API_INSTANCE_ID")
_TOKEN = os.getenv("GREEN_API_TOKEN")
_GROUP_CHAT_ID = os.getenv("WHATSAPP_GROUP_CHAT_ID")


def _base_url(endpoint: str) -> str:
    return f"https://api.green-api.com/waInstance{_INSTANCE_ID}/{endpoint}/{_TOKEN}"


def _check_env() -> bool:
    if not all([_INSTANCE_ID, _TOKEN, _GROUP_CHAT_ID]):
        log.error("Missing GREEN_API_INSTANCE_ID, GREEN_API_TOKEN, or WHATSAPP_GROUP_CHAT_ID env vars")
        return False
    return True


def send_message(text: str) -> bool:
    if not _check_env():
        return False
    try:
        resp = requests.post(
            _base_url("sendMessage"),
            json={"chatId": _GROUP_CHAT_ID, "message": text},
            timeout=15,
        )
        resp.raise_for_status()
        log.info("Message delivered successfully")
        return True
    except requests.RequestException as e:
        log.error("Failed to send WhatsApp message: %s", e)
        return False


def send_gif(gif_url: str) -> bool:
    if not _check_env():
        return False
    try:
        resp = requests.post(
            _base_url("sendFileByUrl"),
            json={"chatId": _GROUP_CHAT_ID, "urlFile": gif_url, "fileName": "reaction.gif"},
            timeout=15,
        )
        resp.raise_for_status()
        log.info("GIF delivered successfully")
        return True
    except requests.RequestException as e:
        log.error("Failed to send GIF: %s", e)
        return False
