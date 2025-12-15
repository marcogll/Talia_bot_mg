# app/modules/print.py

from telegram import Update
from telegram.ext import ContextTypes
from app.permissions import is_admin

async def print_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handles the /print command."""
    chat_id = update.effective_chat.id
    if is_admin(chat_id):
        await update.message.reply_text("This is a restricted command for authorized users.")
    else:
        await update.message.reply_text("You are not authorized to use this command.")
