import os
import logging
import requests

log = logging.getLogger(__name__)

_INSTANCE_ID = os.getenv("GREEN_API_INSTANCE_ID")
_TOKEN = os.getenv("GREEN_API_TOKEN")
_GROUP_CHAT_ID = os.getenv("WHATSAPP_GROUP_CHAT_ID")


def send_message(text: str) -> bool:
    """Send a text message to the configured WhatsApp group."""
    if not all([_INSTANCE_ID, _TOKEN, _GROUP_CHAT_ID]):
        log.error("Missing GREEN_API_INSTANCE_ID, GREEN_API_TOKEN, or WHATSAPP_GROUP_CHAT_ID env vars")
        return False

    url = f"https://api.green-api.com/waInstance{_INSTANCE_ID}/sendMessage/{_TOKEN}"
    payload = {"chatId": _GROUP_CHAT_ID, "message": text}

    try:
        resp = requests.post(url, json=payload, timeout=15)
        resp.raise_for_status()
        log.info("Message delivered successfully")
        return True
    except requests.RequestException as e:
        log.error("Failed to send WhatsApp message: %s", e)
        return False
