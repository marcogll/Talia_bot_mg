# app/permissions.py
# Este script maneja los permisos de los usuarios según su ID de chat de Telegram.

from config import OWNER_CHAT_ID, ADMIN_CHAT_IDS, TEAM_CHAT_IDS

def get_user_role(chat_id):
    """
    Determina el rol de un usuario basado en su ID de chat.
    
    Roles posibles: owner (dueño), admin (administrador), team (equipo), client (cliente).
    """
    chat_id_str = str(chat_id)
    
    # Si el ID coincide con el del dueño
    if chat_id_str == OWNER_CHAT_ID:
        return "owner"
    
    # Si el ID está en la lista de administradores
    if chat_id_str in ADMIN_CHAT_IDS:
        return "admin"
    
    # Si el ID está en la lista del equipo
    if chat_id_str in TEAM_CHAT_IDS:
        return "team"
    
    # Si no es ninguno de los anteriores, es un cliente normal
    return "client"

def is_owner(chat_id):
    """Verifica si un usuario es el dueño."""
    return get_user_role(chat_id) == "owner"

def is_admin(chat_id):
    """Verifica si un usuario es administrador o dueño."""
    return get_user_role(chat_id) in ["owner", "admin"]

def is_team_member(chat_id):
    """Verifica si un usuario es parte del equipo, administrador o dueño."""
    return get_user_role(chat_id) in ["owner", "admin", "team"]
