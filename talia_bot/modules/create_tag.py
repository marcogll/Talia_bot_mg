# app/modules/create_tag.py
# Este módulo permite crear un "tag" (etiqueta) con información del empleado.
# Usa un ConversationHandler para hacer una serie de preguntas al usuario.
# Al final, genera un código en Base64 que contiene toda la información en formato JSON.

import base64
import json
import logging
from telegram import Update
from telegram.ext import (
    ContextTypes,
    ConversationHandler,
    CommandHandler,
    MessageHandler,
    filters,
)

# Configuramos los logs para este archivo
logger = logging.getLogger(__name__)

# Definimos los estados de la conversación.
# Cada número representa un paso en el proceso de preguntas.
NAME, NUM_EMP, SUCURSAL, TELEGRAM_ID = range(4)

async def create_tag_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """
    Inicia el proceso cuando el usuario escribe /create_tag.
    Pide el primer dato: el nombre.
    """
    await update.message.reply_text("Vamos a crear un nuevo tag. Por favor, dime el nombre:")
    # Devolvemos el siguiente estado: NAME
    return NAME

async def get_name(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """
    Guarda el nombre y pide el número de empleado.
    """
    context.user_data['name'] = update.message.text
    await update.message.reply_text("Gracias. Ahora, por favor, dime el número de empleado:")
    # Devolvemos el siguiente estado: NUM_EMP
    return NUM_EMP

async def get_num_emp(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """
    Guarda el número de empleado y pide la sucursal.
    """
    context.user_data['num_emp'] = update.message.text
    await update.message.reply_text("Entendido. Ahora, por favor, dime la sucursal:")
    # Devolvemos el siguiente estado: SUCURSAL
    return SUCURSAL

async def get_sucursal(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """
    Guarda la sucursal y pide el ID de Telegram.
    """
    context.user_data['sucursal'] = update.message.text
    await update.message.reply_text("Perfecto. Finalmente, por favor, dime el ID de Telegram:")
    # Devolvemos el siguiente estado: TELEGRAM_ID
    return TELEGRAM_ID

async def get_telegram_id(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """
    Guarda el ID de Telegram, junta todos los datos y genera el código Base64.
    """
    context.user_data['telegram_id'] = update.message.text

    # Creamos un diccionario (como una caja con etiquetas) con todos los datos
    tag_data = {
        "name": context.user_data.get('name'),
        "num_emp": context.user_data.get('num_emp'),
        "sucursal": context.user_data.get('sucursal'),
        "telegram_id": context.user_data.get('telegram_id'),
    }

    # Convertimos el diccionario a una cadena de texto en formato JSON
    json_string = json.dumps(tag_data)

    # Convertimos esa cadena a Base64 (un formato que se puede guardar en tags NFC)
    # 1. Codificamos a bytes (utf-8)
    # 2. Codificamos esos bytes a base64
    # 3. Convertimos de vuelta a texto para mostrarlo
    base64_bytes = base64.b64encode(json_string.encode('utf-8'))
    base64_string = base64_bytes.decode('utf-8')

    await update.message.reply_text(f"¡Gracias! Aquí está tu tag en formato Base64:\n\n`{base64_string}`", parse_mode='Markdown')

    # Limpiamos los datos temporales del usuario
    context.user_data.clear()

    # Terminamos la conversación
    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """
    Cancela el proceso si el usuario escribe /cancel.
    """
    await update.message.reply_text("Creación de tag cancelada.")
    context.user_data.clear()
    return ConversationHandler.END

def create_tag_conv_handler():
    """
    Configura el manejador de la conversación (el flujo de preguntas).
    """
    return ConversationHandler(
        # Punto de entrada: el comando /create_tag
        entry_points=[CommandHandler('create_tag', create_tag_start)],

        # Mapa de estados: qué función responde a cada paso
        states={
            NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_name)],
            NUM_EMP: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_num_emp)],
            SUCURSAL: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_sucursal)],
            TELEGRAM_ID: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_telegram_id)],
        },

        # Si algo falla o el usuario cancela
        fallbacks=[CommandHandler('cancel', cancel)],

        per_message=False
    )
