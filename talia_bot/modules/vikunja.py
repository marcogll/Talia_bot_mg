# talia_bot/modules/vikunja.py
# Este módulo maneja la integración con Vikunja para la gestión de proyectos y tareas.

import logging
import httpx

from talia_bot.config import VIKUNJA_API_URL, VIKUNJA_API_TOKEN

# Configuración del logger
logger = logging.getLogger(__name__)

def get_vikunja_headers():
    """Devuelve los headers necesarios para la API de Vikunja."""
    return {
        "Authorization": f"Bearer {VIKUNJA_API_TOKEN}",
        "Content-Type": "application/json",
    }

async def get_projects():
    """
    Obtiene la lista de proyectos de Vikunja de forma asíncrona.
    Devuelve una lista de diccionarios de proyectos o None si hay un error.
    """
    if not VIKUNJA_API_TOKEN:
        logger.error("VIKUNJA_API_TOKEN no está configurado.")
        return None

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{VIKUNJA_API_URL}/projects", headers=get_vikunja_headers())
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            logger.error(f"Error de HTTP al obtener proyectos de Vikunja: {e.response.status_code} - {e.response.text}")
            return None
        except Exception as e:
            logger.error(f"Error al obtener proyectos de Vikunja: {e}")
            return None

async def get_project_tasks(project_id: int):
    """
    Obtiene las tareas de un proyecto específico de forma asíncrona.
    """
    if not VIKUNJA_API_TOKEN:
        logger.error("VIKUNJA_API_TOKEN no está configurado.")
        return None

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{VIKUNJA_API_URL}/projects/{project_id}/tasks", headers=get_vikunja_headers())
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            logger.error(f"Error de HTTP al obtener tareas del proyecto {project_id}: {e.response.status_code}")
            return None
        except Exception as e:
            logger.error(f"Error al obtener tareas del proyecto {project_id}: {e}")
            return None

async def add_comment_to_task(task_id: int, comment: str):
    """
    Añade un comentario a una tarea específica.
    """
    if not VIKUNJA_API_TOKEN:
        logger.error("VIKUNJA_API_TOKEN no está configurado.")
        return False

    async with httpx.AsyncClient() as client:
        try:
            data = {"comment": comment}
            response = await client.post(f"{VIKUNJA_API_URL}/tasks/{task_id}/comments", headers=get_vikunja_headers(), json=data)
            response.raise_for_status()
            logger.info(f"Comentario añadido a la tarea {task_id}.")
            return True
        except httpx.HTTPStatusError as e:
            logger.error(f"Error de HTTP al añadir comentario a la tarea {task_id}: {e.response.status_code}")
            return False
        except Exception as e:
            logger.error(f"Error al añadir comentario a la tarea {task_id}: {e}")
            return False

async def update_task_status(task_id: int, is_done: bool = None, status_text: str = None):
    """
    Actualiza una tarea en Vikunja.
    - Si `is_done` es un booleano, actualiza el estado de completado.
    - Si `status_text` es un string, añade un comentario con ese estado.
    """
    if not VIKUNJA_API_TOKEN:
        logger.error("VIKUNJA_API_TOKEN no está configurado.")
        return False

    async with httpx.AsyncClient() as client:
        try:
            if is_done is not None:
                data = {"done": is_done}
                response = await client.put(f"{VIKUNJA_API_URL}/tasks/{task_id}", headers=get_vikunja_headers(), json=data)
                response.raise_for_status()
                logger.info(f"Estado de la tarea {task_id} actualizado a {'completado' if is_done else 'pendiente'}.")
                return True

            if status_text:
                return await add_comment_to_task(task_id, f"Nuevo estatus: {status_text}")

        except httpx.HTTPStatusError as e:
            logger.error(f"Error de HTTP al actualizar la tarea {task_id}: {e.response.status_code}")
            return False
        except Exception as e:
            logger.error(f"Error al actualizar la tarea {task_id}: {e}")
            return False
    return False

async def create_task(project_id: int, title: str, due_date: str = None):
    """
    Crea una nueva tarea en un proyecto específico.
    """
    if not VIKUNJA_API_TOKEN:
        logger.error("VIKUNJA_API_TOKEN no está configurado.")
        return None

    async with httpx.AsyncClient() as client:
        try:
            data = {"project_id": project_id, "title": title}
            if due_date:
                data["due_date"] = due_date

            response = await client.post(f"{VIKUNJA_API_URL}/tasks", headers=get_vikunja_headers(), json=data)
            response.raise_for_status()
            task = response.json()
            logger.info(f"Tarea '{title}' creada en el proyecto {project_id}.")
            return task
        except httpx.HTTPStatusError as e:
            logger.error(f"Error de HTTP al crear la tarea: {e.response.status_code}")
            return None
        except Exception as e:
            logger.error(f"Error al crear la tarea: {e}")
            return None
