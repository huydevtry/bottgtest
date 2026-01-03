import os
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")
APP_NAME = os.getenv("APP_NAME", "bottgtest")
USERNAME = os.getenv("INSTA_USER")
PASSWORD = os.getenv("INSTA_PASS")


#Telegram bot token
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


if not API_TOKEN:
    raise RuntimeError("API_TOKEN is required")