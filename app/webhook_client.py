# app/webhook_client.py

import requests
from config import N8N_WEBHOOK_URL

def send_webhook(event_data):
    """
    Sends a webhook to the n8n service.
    """
    try:
        response = requests.post(N8N_WEBHOOK_URL, json=event_data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error sending webhook: {e}")
        return None
