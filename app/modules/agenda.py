# app/modules/agenda.py

def get_agenda():
    """
    Fetches and displays the user's agenda for today.
    For now, it returns a hardcoded sample agenda.
    """
    # TODO: Fetch agenda from Google Calendar
    agenda_text = (
        "📅 *Agenda para Hoy*\n\n"
        "• *10:00 AM - 11:00 AM*\n"
        "  Reunión de Sincronización - Proyecto A\n\n"
        "• *12:30 PM - 1:30 PM*\n"
        "  Llamada con Cliente B\n\n"
        "• *4:00 PM - 5:00 PM*\n"
        "  Bloque de trabajo profundo - Desarrollo Talía"
    )
    return agenda_text
