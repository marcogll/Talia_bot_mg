# app/modules/servicios.py
# Este módulo se encarga de dar información sobre los servicios ofrecidos.
# Es un módulo informativo para los clientes.

def get_service_info():
    """
    Muestra una lista breve de los servicios disponibles.
    
    Por ahora devuelve un texto fijo. Se podría conectar a una base de datos
    para que sea más fácil de actualizar.
    """
    # TODO: Obtener detalles de servicios desde una base de datos o archivo de configuración.
    return "Ofrecemos una variedad de servicios, incluyendo:\n\n- Consultoría Estratégica\n- Desarrollo de Software\n- Talleres de Capacitación\n\n¿Sobre cuál te gustaría saber más?"
