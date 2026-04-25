"""Run this to find your WhatsApp group chat ID."""
import os
import requests
from dotenv import load_dotenv

load_dotenv()

instance_id = os.getenv("GREEN_API_INSTANCE_ID")
token = os.getenv("GREEN_API_TOKEN")

url = f"https://api.green-api.com/waInstance{instance_id}/getChats/{token}"
resp = requests.get(url, timeout=15)
chats = resp.json()

print("\nYour WhatsApp chats:\n")
for chat in chats:
    name = chat.get("name") or chat.get("id")
    chat_id = chat.get("id", "")
    if "@g.us" in chat_id:  # groups only
        print(f"GROUP  | {name}")
        print(f"ID     | {chat_id}")
        print("-" * 40)
