# app/modules/admin.py
# Este módulo contiene funciones administrativas para el bot.
# Por ahora, permite ver el estado general del sistema.

def get_system_status():
    """
    Devuelve un mensaje con el estado actual del bot y sus conexiones.
    
    Actualmente el mensaje es fijo (hardcoded), pero en el futuro podría
    hacer pruebas reales de conexión.
    """
    # TODO: Implementar pruebas de estado en tiempo real para un monitoreo exacto.
    status_text = (
        "📊 *Estado del Sistema*\n\n"
        "- *Bot Principal:* Activo ✅\n"
        "- *Conexión Telegram API:* Estable ✅\n"
        "- *Integración n8n:* Operacional ✅\n"
        "- *Google Calendar:* Conectado ✅"
    )
    return status_text
