# app/modules/equipo.py
# Este módulo contiene funciones para los miembros autorizados del equipo.
# Incluye un flujo para proponer actividades que el dueño debe aprobar.

def view_requests_status():
    """
    Permite a un miembro del equipo ver el estado de sus solicitudes recientes.
    
    Por ahora devuelve un estado de ejemplo fijo.
    """
    # TODO: Obtener el estado real desde una base de datos.
    return "Aquí está el estado de tus solicitudes recientes:\n\n- Grabación de proyecto (4h): Aprobado\n- Taller de guion (2h): Pendiente"
