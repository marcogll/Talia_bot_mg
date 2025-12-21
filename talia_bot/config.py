# talia_bot/config.py
# Este archivo se encarga de cargar todas las variables de entorno y configuraciones del bot.
# Las variables de entorno son valores que se guardan fuera del código por seguridad (como tokens y llaves API).

import os
from dotenv import load_dotenv
from pathlib import Path

# Cargar variables de entorno desde el archivo .env en la raíz del proyecto
env_path = Path(__file__).parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

# --- TELEGRAM & SECURITY ---
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
# Prioriza ADMIN_ID, pero usa OWNER_CHAT_ID como fallback para compatibilidad
ADMIN_ID = os.getenv("ADMIN_ID") or os.getenv("OWNER_CHAT_ID")
CREW_CHAT_IDS = os.getenv("CREW_CHAT_IDS", "").split(',')

# --- AI CORE ---
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")

# --- INTEGRACIONES ---
# Google
GOOGLE_SERVICE_ACCOUNT_FILE = os.getenv("GOOGLE_SERVICE_ACCOUNT_FILE")
if GOOGLE_SERVICE_ACCOUNT_FILE and not os.path.isabs(GOOGLE_SERVICE_ACCOUNT_FILE):
    GOOGLE_SERVICE_ACCOUNT_FILE = str(Path(__file__).parent.parent / GOOGLE_SERVICE_ACCOUNT_FILE)
CALENDAR_ID = os.getenv("CALENDAR_ID")

# Vikunja
VIKUNJA_API_URL = os.getenv("VIKUNJA_BASE_URL")
VIKUNJA_API_TOKEN = os.getenv("VIKUNJA_TOKEN")
VIKUNJA_INBOX_PROJECT_ID = os.getenv("VIKUNJA_INBOX_PROJECT_ID")

# n8n
N8N_WEBHOOK_URL = os.getenv("N8N_WEBHOOK_URL")
N8N_TEST_WEBHOOK_URL = os.getenv("N8N_WEBHOOK-TEST_URL")

# --- PRINT SERVICE (SMTP/IMAP) ---
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

IMAP_SERVER = os.getenv("IMAP_SERVER")
IMAP_USER = os.getenv("IMAP_USER")
IMAP_PASSWORD = os.getenv("IMAP_PASSWORD")
PRINTER_EMAIL = os.getenv("PRINTER_EMAIL")

# --- OTROS ---
DAILY_SUMMARY_TIME = os.getenv("DAILY_SUMMARY_TIME", "07:00")
CALENDLY_LINK = os.getenv("CALENDLY_LINK", "https://calendly.com/user/appointment-link")
TIMEZONE = os.getenv("TIMEZONE", "America/Mexico_City")
