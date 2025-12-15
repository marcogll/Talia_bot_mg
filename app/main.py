# app/main.py
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

from config import TELEGRAM_BOT_TOKEN
from permissions import get_user_role
from modules.onboarding import handle_start as onboarding_handle_start
from modules.agenda import get_agenda
from modules.citas import request_appointment
from modules.equipo import propose_activity, view_requests_status
from modules.aprobaciones import approve_request, view_pending
from modules.servicios import get_service_info

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a welcome message and menu when the /start command is issued."""
    chat_id = update.effective_chat.id
    user_role = get_user_role(chat_id)

    logger.info(f"User {chat_id} started conversation with role: {user_role}")

    # Delegate to the onboarding module
    response_text, reply_markup = onboarding_handle_start(user_role)

    await update.message.reply_text(response_text, reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and calls the appropriate module."""
    query = update.callback_query
    await query.answer()

    logger.info(f"Received callback query: {query.data}")

    response_text = "Acción no reconocida."

    if query.data == 'view_agenda':
        response_text = get_agenda()
    elif query.data == 'view_pending':
        response_text = view_pending()
    elif query.data == 'approve_request':
        response_text = approve_request()
    elif query.data == 'propose_activity':
        response_text = propose_activity()
    elif query.data == 'view_requests_status':
        response_text = view_requests_status()
    elif query.data == 'schedule_appointment':
        response_text = request_appointment()
    elif query.data == 'get_service_info':
        response_text = get_service_info()

    await query.edit_message_text(text=response_text, parse_mode='Markdown')

def main() -> None:
    """Start the bot."""
    if not TELEGRAM_BOT_TOKEN:
        logger.error("TELEGRAM_BOT_TOKEN is not set in the environment variables.")
        return

    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))

    # Run the bot until the user presses Ctrl-C
    logger.info("Starting Talía Bot...")
    application.run_polling()

if __name__ == "__main__":
    main()
