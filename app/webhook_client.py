# app/webhook_client.py
# Este script se encarga de enviar datos a servicios externos usando "webhooks".
# En este caso, se comunica con n8n.

import requests
from config import N8N_WEBHOOK_URL

def send_webhook(event_data):
    """
    Envía datos de un evento al servicio n8n.
    
    Parámetros:
    - event_data: Un diccionario con la información que queremos enviar.
    """
    try:
        # Hacemos una petición POST (enviar datos) a la URL configurada
        response = requests.post(N8N_WEBHOOK_URL, json=event_data)
        # Verificamos si la petición fue exitosa (status code 200-299)
        response.raise_for_status()
        # Devolvemos la respuesta del servidor en formato JSON
        return response.json()
    except requests.exceptions.RequestException as e:
        # Si hay un error en la conexión o el envío, lo mostramos
        print(f"Error al enviar el webhook: {e}")
        return None
