# app/scheduler.py
# Este script se encarga de programar tareas automáticas, como el resumen diario.

import logging
from datetime import time
from telegram.ext import ContextTypes
import pytz

from config import OWNER_CHAT_ID, TIMEZONE, DAILY_SUMMARY_TIME
from modules.agenda import get_agenda

# Configuramos el registro de eventos (logging) para ver qué pasa en la consola
logger = logging.getLogger(__name__)

async def send_daily_summary(context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Función que envía el resumen diario al dueño del bot.
    Se ejecuta automáticamente según lo programado.
    """
    job = context.job
    chat_id = job.chat_id

    logger.info(f"Ejecutando tarea de resumen diario para el chat_id: {chat_id}")

    try:
        # Obtenemos la agenda del día
        agenda_text = get_agenda()
        # Preparamos el mensaje
        summary_text = f"🔔 *Resumen Diario - Buen día, Marco!*\n\n{agenda_text}"

        # Enviamos el mensaje por Telegram
        await context.bot.send_message(
            chat_id=chat_id,
            text=summary_text,
            parse_mode='Markdown'
        )
        logger.info(f"Resumen diario enviado con éxito a {chat_id}")
    except Exception as e:
        # Si hay un error, lo registramos
        logger.error(f"Error al enviar el resumen diario a {chat_id}: {e}")

def schedule_daily_summary(application) -> None:
    """
    Programa la tarea del resumen diario para que ocurra todos los días.
    """
    # Si no hay un ID de dueño configurado, no programamos nada
    if not OWNER_CHAT_ID:
        logger.warning("OWNER_CHAT_ID no configurado. No se programará el resumen diario.")
        return

    job_queue = application.job_queue

    # Configuramos la zona horaria (ej. America/Mexico_City)
    tz = pytz.timezone(TIMEZONE)

    # Obtenemos la hora y minutos desde la configuración (ej. "07:00")
    try:
        hour, minute = map(int, DAILY_SUMMARY_TIME.split(':'))
    except ValueError:
        logger.error(f"Formato de DAILY_SUMMARY_TIME inválido: {DAILY_SUMMARY_TIME}. Usando 07:00 por defecto.")
        hour, minute = 7, 0

    # Programamos la tarea para que corra todos los días a la hora configurada
    scheduled_time = time(hour=hour, minute=minute, tzinfo=tz)

    job_queue.run_daily(
        send_daily_summary,
        time=scheduled_time,
        chat_id=int(OWNER_CHAT_ID),
        name="daily_summary"
    )

    logger.info(f"Resumen diario programado para {OWNER_CHAT_ID} a las {scheduled_time} ({TIMEZONE})")
