# app/permissions.py

from config import OWNER_CHAT_ID, ADMIN_CHAT_IDS, TEAM_CHAT_IDS

def get_user_role(chat_id):
    """
    Determines the role of a user based on their chat ID.
    """
    chat_id_str = str(chat_id)
    if chat_id_str == OWNER_CHAT_ID:
        return "owner"
    if chat_id_str in ADMIN_CHAT_IDS:
        return "admin"
    if chat_id_str in TEAM_CHAT_IDS:
        return "team"
    return "client"

def is_owner(chat_id):
    """
    Checks if a user is the owner.
    """
    return get_user_role(chat_id) == "owner"

def is_admin(chat_id):
    """
    Checks if a user is an admin.
    """
    return get_user_role(chat_id) in ["owner", "admin"]

def is_team_member(chat_id):
    """
    Checks if a user is a team member.
    """
    return get_user_role(chat_id) in ["owner", "admin", "team"]
