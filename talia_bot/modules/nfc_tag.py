# talia_bot/modules/nfc_tag.py
# This module contains the logic for generating NFC tags.

import base64
import json
import logging

logger = logging.getLogger(__name__)

def generate_nfc_tag(collected_data):
    """
    Generates a Base64 encoded string from the collected data.
    """
    tag_data = {
        "name": collected_data.get("EMPLOYEE_NAME"),
        "num_emp": collected_data.get("EMPLOYEE_ID"),
        "sucursal": collected_data.get("BRANCH"),
        "telegram_id": collected_data.get("TELEGRAM_ID"),
    }

    json_string = json.dumps(tag_data)
    base64_bytes = base64.b64encode(json_string.encode("utf-8"))
    base64_string = base64_bytes.decode("utf-8")

    return f"¡Gracias! Aquí está tu tag en formato Base64:\n\n`{base64_string}`"
