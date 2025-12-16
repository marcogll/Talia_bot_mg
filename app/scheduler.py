# app/scheduler.py
import logging
from datetime import time
from telegram.ext import ContextTypes
import pytz

from app.config import OWNER_CHAT_ID, TIMEZONE
from app.modules.agenda import get_agenda

# Enable logging
logger = logging.getLogger(__name__)

async def send_daily_summary(context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends the daily summary to the owner."""
    job = context.job
    chat_id = job.chat_id

    logger.info(f"Running daily summary job for chat_id: {chat_id}")

    try:
        agenda_text = get_agenda()
        summary_text = f"🔔 *Resumen Diario - Buen día, Marco!*\n\n{agenda_text}"

        await context.bot.send_message(
            chat_id=chat_id,
            text=summary_text,
            parse_mode='Markdown'
        )
        logger.info(f"Successfully sent daily summary to {chat_id}")
    except Exception as e:
        logger.error(f"Failed to send daily summary to {chat_id}: {e}")

def schedule_daily_summary(application) -> None:
    """Schedules the daily summary job."""
    if not OWNER_CHAT_ID:
        logger.warning("OWNER_CHAT_ID not set. Daily summary will not be scheduled.")
        return

    job_queue = application.job_queue

    # Use the timezone from config
    tz = pytz.timezone(TIMEZONE)

    # Schedule the job to run every day at 7:00 AM
    scheduled_time = time(hour=7, minute=0, tzinfo=tz)

    job_queue.run_daily(
        send_daily_summary,
        time=scheduled_time,
        chat_id=int(OWNER_CHAT_ID),
        name="daily_summary"
    )

    logger.info(f"Scheduled daily summary for {OWNER_CHAT_ID} at {scheduled_time} {TIMEZONE}")
