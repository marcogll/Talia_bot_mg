# talia_bot/modules/imap_listener.py
import imaplib
import email
import json
import logging
from email.header import decode_header

from talia_bot.config import IMAP_SERVER, IMAP_USER, IMAP_PASSWORD

logger = logging.getLogger(__name__)

def check_for_confirmation(job_id: str):
    """
    Checks for a print confirmation email via IMAP.
    Returns the parsed data from the email subject if a confirmation is found, else None.
    """
    if not all([IMAP_SERVER, IMAP_USER, IMAP_PASSWORD]):
        logger.error("IMAP settings are not fully configured.")
        return None

    try:
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)
        mail.login(IMAP_USER, IMAP_PASSWORD)
        mail.select("inbox")

        # Buscar correos no leídos del remitente específico
        status, messages = mail.search(None, '(UNSEEN FROM "noreply@print.epsonconnect.com")')
        if status != "OK":
            logger.error("Failed to search for emails.")
            mail.logout()
            return None

        for num in messages[0].split():
            status, data = mail.fetch(num, "(RFC822)")
            if status != "OK":
                continue

            msg = email.message_from_bytes(data[0][1])

            # Decodificar el asunto del correo
            subject, encoding = decode_header(msg["Subject"])[0]
            if isinstance(subject, bytes):
                subject = subject.decode(encoding if encoding else "utf-8")

            # Buscar la línea que contiene el asunto original
            body = ""
            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/plain":
                        body = part.get_payload(decode=True).decode()
                        break
            else:
                body = msg.get_payload(decode=True).decode()

            for line in body.splitlines():
                if line.strip().startswith("Subject:"):
                    original_subject = line.strip()[len("Subject:"):].strip()
                    # El asunto está encapsulado en `DATA:{...}`
                    if original_subject.startswith("DATA:"):
                        try:
                            json_data_str = original_subject[len("DATA:"):].strip()
                            job_data = json.loads(json_data_str)

                            if job_data.get("job_id") == job_id:
                                logger.info(f"Confirmation found for job_id: {job_id}")
                                # Marcar el correo como leído
                                mail.store(num, '+FLAGS', '\\Seen')
                                mail.logout()
                                return job_data
                        except (json.JSONDecodeError, KeyError) as e:
                            logger.warning(f"Could not parse job data from subject: {original_subject}. Error: {e}")
                            continue

        mail.logout()
        return None

    except Exception as e:
        logger.error(f"Failed to check email via IMAP: {e}")
        return None
