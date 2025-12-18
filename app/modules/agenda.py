# app/modules/agenda.py
# Este módulo se encarga de manejar las peticiones relacionadas con la agenda.
# Permite obtener y mostrar las actividades programadas para el día.

def get_agenda():
    """
    Obtiene y muestra la agenda del usuario para el día actual.
    
    Por ahora, esta función devuelve una agenda de ejemplo fija.
    El plan es conectarla con Google Calendar para que sea real.
    """
    # TODO: Obtener la agenda dinámicamente desde Google Calendar.
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
