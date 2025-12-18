# app/modules/citas.py
# Este módulo maneja la programación de citas para los clientes.
# Permite a los usuarios obtener un enlace para agendar una reunión.

def request_appointment():
    """
    Proporciona al usuario un enlace para agendar una cita.
    
    Por ahora devuelve un enlace de ejemplo a Calendly.
    La idea es que sea un enlace dinámico generado por n8n.
    """
    # TODO: Integrar con un servicio real o un flujo de n8n para dar un enlace personalizado.
    response_text = (
        "Para agendar una cita, por favor utiliza el siguiente enlace: \n\n"
        "[Enlace de Calendly](https://calendly.com/user/appointment-link)"
    )
    return response_text
