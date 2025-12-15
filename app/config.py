# app/config.py
import os

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OWNER_CHAT_ID = os.getenv("OWNER_CHAT_ID")
ADMIN_CHAT_IDS = os.getenv("ADMIN_CHAT_IDS", "").split(",")
TEAM_CHAT_IDS = os.getenv("TEAM_CHAT_IDS", "").split(",")
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
GOOGLE_REFRESH_TOKEN = os.getenv("GOOGLE_REFRESH_TOKEN")
N8N_WEBHOOK_URL = os.getenv("N8N_WEBHOOK_URL")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TIMEZONE = os.getenv("TIMEZONE", "America/Mexico_City")
