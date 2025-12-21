# talia_bot/modules/sales_rag.py
# This module will contain the sales RAG flow for new clients.

import json
import logging
from talia_bot.modules.llm_engine import get_smart_response

logger = logging.getLogger(__name__)

def load_services_data():
    """Loads the services data from the JSON file."""
    try:
        with open("talia_bot/data/services.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        logger.error("El archivo services.json no fue encontrado.")
        return []
    except json.JSONDecodeError:
        logger.error("Error al decodificar el archivo services.json.")
        return []

def find_relevant_services(user_query, services):
    """
    Finds relevant services based on the user's query.
    A simple keyword matching approach is used here.
    """
    query = user_query.lower()
    relevant_services = []
    for service in services:
        for keyword in service.get("keywords", []):
            if keyword in query:
                relevant_services.append(service)
                break  # Avoid adding the same service multiple times
    return relevant_services

def generate_sales_pitch(user_query, collected_data):
    """
    Generates a personalized sales pitch using the RAG approach.
    """
    services = load_services_data()
    relevant_services = find_relevant_services(user_query, services)

    if not relevant_services:
        # Fallback if no specific services match
        context_str = "No specific services match the user's request, but we can offer general business consulting."
    else:
        context_str = "Based on your needs, here are some services we offer:\n"
        for service in relevant_services:
            context_str += f"- **{service['service_name']}**: {service['description']}\n"

    prompt = (
        f"El cliente {collected_data.get('CLIENT_NAME', 'un cliente')} "
        f"del sector {collected_data.get('CLIENT_INDUSTRY', 'no especificado')} "
        f"ha descrito su proyecto de la siguiente manera: '{user_query}'.\n\n"
        f"Aquí hay información sobre nuestros servicios que podría ser relevante para ellos:\n{context_str}\n\n"
        "Actúa como un asistente de ventas amigable y experto llamado Talia. "
        "Tu objetivo es conectar su idea con nuestros servicios y proponer los siguientes pasos. "
        "Genera una respuesta personalizada que:\n"
        "1. Muestre que has entendido su idea.\n"
        "2. Destaque cómo nuestros servicios pueden ayudarles a alcanzar sus objetivos.\n"
        "3. Termine con una llamada a la acción clara, como sugerir una llamada o una reunión para discutirlo más a fondo."
    )

    return get_smart_response(prompt)
