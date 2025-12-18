# app/modules/onboarding.py
# Este módulo maneja la primera interacción con el usuario (el comando /start).
# Se encarga de mostrar un menú diferente según quién sea el usuario (dueño, admin, equipo o cliente).

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def get_owner_menu():
    """Crea el menú de botones para el Dueño (Owner)."""
    keyboard = [
        [InlineKeyboardButton("📅 Ver mi agenda", callback_data='view_agenda')],
        [InlineKeyboardButton("⏳ Ver pendientes", callback_data='view_pending')],
    ]
    return InlineKeyboardMarkup(keyboard)

def get_admin_menu():
    """Crea el menú de botones para los Administradores."""
    keyboard = [
        [InlineKeyboardButton("📊 Ver estado del sistema", callback_data='view_system_status')],
        [InlineKeyboardButton("👥 Gestionar usuarios", callback_data='manage_users')],
    ]
    return InlineKeyboardMarkup(keyboard)

def get_team_menu():
    """Crea el menú de botones para los Miembros del Equipo."""
    keyboard = [
        [InlineKeyboardButton("🕒 Proponer actividad", callback_data='propose_activity')],
        [InlineKeyboardButton("📄 Ver estatus de solicitudes", callback_data='view_requests_status')],
    ]
    return InlineKeyboardMarkup(keyboard)

def get_client_menu():
    """Crea el menú de botones para los Clientes externos."""
    keyboard = [
        [InlineKeyboardButton("🗓️ Agendar una cita", callback_data='schedule_appointment')],
        [InlineKeyboardButton("ℹ️ Información de servicios", callback_data='get_service_info')],
    ]
    return InlineKeyboardMarkup(keyboard)

def handle_start(user_role):
    """
    Decide qué mensaje y qué menú mostrar según el rol del usuario.
    """
    welcome_message = "Hola, soy Talía. ¿En qué puedo ayudarte hoy?"

    # Dependiendo del rol, llamamos a una función de menú diferente
    if user_role == "owner":
        menu = get_owner_menu()
    elif user_role == "admin":
        menu = get_admin_menu()
    elif user_role == "team":
        menu = get_team_menu()
    else: # Por defecto, si no es ninguno de los anteriores, es un cliente
        menu = get_client_menu()

    return welcome_message, menu
