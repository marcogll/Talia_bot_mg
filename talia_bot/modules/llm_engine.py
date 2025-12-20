# talia_bot/modules/llm_engine.py
# Este script se encarga de la comunicación con la inteligencia artificial de OpenAI.

import openai
import json
import logging
from talia_bot.config import OPENAI_API_KEY, OPENAI_MODEL

logger = logging.getLogger(__name__)

async def get_smart_response(prompt: str, system_message: str = "Eres un asistente útil.") -> str:
    """
    Genera una respuesta inteligente usando la API de OpenAI de forma asíncrona.
    """
    if not OPENAI_API_KEY:
        logger.error("OPENAI_API_KEY no está configurada.")
        return "Error: La llave de la API de OpenAI no está configurada."

    try:
        client = openai.AsyncOpenAI(api_key=OPENAI_API_KEY)
        
        response = await client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": prompt},
            ],
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        logger.error(f"Ocurrió un error al comunicarse con OpenAI: {e}")
        return f"Ocurrió un error al comunicarse con OpenAI: {e}"

async def analyze_client_pitch(pitch: str, display_name: str) -> str:
    """
    Analiza el pitch de un cliente contra una lista de servicios y genera una respuesta de ventas.
    """
    try:
        with open('talia_bot/data/services.json', 'r', encoding='utf-8') as f:
            services = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.error(f"Error al cargar o decodificar services.json: {e}")
        return "Lo siento, estoy teniendo problemas para acceder a nuestra lista de servicios en este momento."

    services_description = "\n".join([f"- {s['service_name']}: {s['description']}" for s in services])

    system_message = f"""
    Eres Talia, la asistente personal de {display_name}. Tu objetivo es actuar como un filtro de ventas inteligente.
    Analiza la necesidad del cliente y compárala con la lista de servicios que ofrece {display_name}.
    Tu respuesta debe seguir estas reglas estrictamente:
    1.  Identifica cuál de los servicios de la lista es el más adecuado para la necesidad del cliente.
    2.  Confirma que el proyecto del cliente es interesante y encaja perfectamente con el servicio que identificaste. Menciona el nombre del servicio.
    3.  Cierra la conversación de manera profesional y tranquilizadora, indicando que ya has pasado el expediente a {display_name} y que él lo revisará personalmente.
    4.  Sé concisa, profesional y amable. No hagas preguntas, solo proporciona la respuesta de cierre.
    """

    prompt = f"""
    **Servicios Ofrecidos:**
    {services_description}

    **Necesidad del Cliente:**
    "{pitch}"

    **Tu Tarea:**
    Genera la respuesta de cierre ideal siguiendo las reglas del system prompt.
    """

    return await get_smart_response(prompt, system_message)
