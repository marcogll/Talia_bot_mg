# app/config.py
# Este archivo se encarga de cargar todas las variables de entorno y configuraciones del bot.
# Las variables de entorno son valores que se guardan fuera del código por seguridad (como tokens y llaves API).

import os

# Token del bot de Telegram (obtenido de @BotFather)
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# ID de chat del dueño del bot (para recibir notificaciones importantes)
OWNER_CHAT_ID = os.getenv("OWNER_CHAT_ID")

# IDs de chat de los administradores, separados por comas en el archivo .env
ADMIN_CHAT_IDS = os.getenv("ADMIN_CHAT_IDS", "").split(",")

# IDs de chat del equipo de trabajo, separados por comas
TEAM_CHAT_IDS = os.getenv("TEAM_CHAT_IDS", "").split(",")

# Ruta al archivo de credenciales de la cuenta de servicio de Google
GOOGLE_SERVICE_ACCOUNT_FILE = os.getenv("GOOGLE_SERVICE_ACCOUNT_FILE")

# ID del calendario de Google que usará el bot
CALENDAR_ID = os.getenv("CALENDAR_ID")

# URL del webhook de n8n para enviar datos a otros servicios
N8N_WEBHOOK_URL = os.getenv("N8N_WEBHOOK_URL")

# Llave de la API de OpenAI para usar modelos de lenguaje (como GPT)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Zona horaria por defecto para el manejo de fechas y horas
TIMEZONE = os.getenv("TIMEZONE", "America/Mexico_City")
