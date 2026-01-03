# app/telegram/handler.py
import requests
from app.core.config import TELEGRAM_BOT_TOKEN

BASE_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}"

def send_message(chat_id: int, text: str):
    requests.post(
        f"{BASE_URL}/sendMessage",
        json={"chat_id": chat_id, "text": text},
        timeout=5,
    )

def handle_update(update):
    if not update.message or not update.message.text:
        return

    chat_id = update.message.chat.id
    text = update.message.text.strip()

    if text == "/start":
        send_message(chat_id, "👋 Hello! Bot is running.")
    else:
        send_message(chat_id, f"Echo: {text}")
