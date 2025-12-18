# app/modules/aprobaciones.py
# Este módulo gestiona el flujo de aprobación para las solicitudes hechas por el equipo.
# Permite ver solicitudes pendientes y aprobarlas o rechazarlas.
# El usuario principal aquí es el "owner" (dueño).

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def get_approval_menu(request_id):
    """
    Crea un menú de botones (teclado en línea) con "Aprobar" y "Rechazar".
    
    Cada botón lleva el ID de la solicitud para saber cuál estamos procesando.
    """
    keyboard = [
        [
            # callback_data es lo que el bot recibe cuando se pulsa el botón
            InlineKeyboardButton("✅ Aprobar", callback_data=f'approve:{request_id}'),
            InlineKeyboardButton("❌ Rechazar", callback_data=f'reject:{request_id}'),
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

def view_pending():
    """
    Muestra al dueño una lista de solicitudes que esperan su aprobación.
    
    Por ahora usa una lista fija de ejemplo.
    """
    # TODO: Obtener solicitudes reales desde una base de datos o servicio externo.
    proposals = [
        {"id": "prop_001", "desc": "Grabación de proyecto", "duration": 4, "user": "Equipo A"},
        {"id": "prop_002", "desc": "Taller de guion", "duration": 2, "user": "Equipo B"},
    ]

    if not proposals:
        return "No hay solicitudes pendientes.", None

    # Tomamos la primera propuesta para mostrarla
    proposal = proposals[0]

    text = (
        f"⏳ *Nueva Solicitud Pendiente*\n\n"
        f"🙋‍♂️ *Solicitante:* {proposal['user']}\n"
        f"📝 *Actividad:* {proposal['desc']}\n"
        f"⏳ *Duración:* {proposal['duration']} horas"
    )

    # Adjuntamos los botones de aprobación
    reply_markup = get_approval_menu(proposal['id'])

    return text, reply_markup

def handle_approval_action(callback_data):
    """
    Maneja la respuesta del dueño (clic en aprobar o rechazar).
    
    Separa la acción (approve/reject) del ID de la solicitud.
    """
    # callback_data viene como "accion:id", por ejemplo "approve:prop_001"
    action, request_id = callback_data.split(':')

    if action == 'approve':
        # TODO: Guardar en base de datos que fue aprobada y avisar al equipo.
        return f"✅ La solicitud *{request_id}* ha sido aprobada."
    elif action == 'reject':
        # TODO: Guardar en base de datos que fue rechazada y avisar al equipo.
        return f"❌ La solicitud *{request_id}* ha sido rechazada."

    return "Acción desconocida.", None
