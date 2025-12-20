# talia_bot/modules/debug.py
# Este módulo permite a los administradores imprimir los detalles de configuración del bot.
# Es una herramienta útil para depuración (debugging).

from telegram import Update
from telegram.ext import ContextTypes
from talia_bot.modules.identity import is_admin
from talia_bot.config import TIMEZONE, CALENDAR_ID, N8N_WEBHOOK_URL

async def print_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Maneja el comando /print.
    
    Verifica si el usuario es administrador. Si lo es, muestra valores clave
    de la configuración (Zona horaria, ID de calendario, Webhook).
    """
    chat_id = update.effective_chat.id
    
    # Solo permitimos esto a los administradores
    if is_admin(chat_id):
        config_details = (
            f"**Detalles de Configuración**\n"
            f"Zona Horaria: `{TIMEZONE}`\n"
            f"ID de Calendario: `{CALENDAR_ID}`\n"
            f"URL Webhook n8n: `{N8N_WEBHOOK_URL}`\n"
        )
        await update.message.reply_text(config_details, parse_mode='Markdown')
    else:
        # Si no es admin, le avisamos que no tiene permiso
        await update.message.reply_text("No tienes autorización para usar este comando.")
