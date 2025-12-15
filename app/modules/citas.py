# app/modules/citas.py

def request_appointment():
    """
    Provides a link for scheduling an appointment.
    """
    # TODO: Integrate with a real scheduling service or n8n workflow
    response_text = (
        "Para agendar una cita, por favor utiliza el siguiente enlace: \n\n"
        "[Enlace de Calendly](https://calendly.com/user/appointment-link)"
    )
    return response_text
