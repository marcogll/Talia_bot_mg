# talia_bot/modules/mailer.py
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import logging
import asyncio

from talia_bot.config import (
    SMTP_SERVER, SMTP_PORT, SMTP_USER, SMTP_PASSWORD,
    IMAP_USER, PRINTER_EMAIL
)

logger = logging.getLogger(__name__)

async def send_email_with_attachment(file_content: bytes, filename: str, subject: str):
    """
    Sends an email with an attachment using SMTP.
    Adapts connection method based on SMTP_PORT.
    """
    if not all([SMTP_SERVER, SMTP_PORT, SMTP_USER, SMTP_PASSWORD, PRINTER_EMAIL]):
        logger.error("SMTP settings are not fully configured.")
        return False

    message = MIMEMultipart()
    message["From"] = IMAP_USER
    message["To"] = PRINTER_EMAIL
    message["Subject"] = subject

    part = MIMEBase("application", "octet-stream")
    part.set_payload(file_content)
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )
    message.attach(part)
    text = message.as_string()

    try:
        context = ssl.create_default_context()

        def _send_mail():
            if SMTP_PORT == 465:
                # Use SMTP_SSL for port 465
                with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=context) as server:
                    server.login(SMTP_USER, SMTP_PASSWORD)
                    server.sendmail(IMAP_USER, PRINTER_EMAIL, text)
            else:
                # Use STARTTLS for other ports like 587
                with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                    server.starttls(context=context)
                    server.login(SMTP_USER, SMTP_PASSWORD)
                    server.sendmail(IMAP_USER, PRINTER_EMAIL, text)

            logger.info(f"Email sent to {PRINTER_EMAIL} for printing.")

        await asyncio.to_thread(_send_mail)
        return True

    except Exception as e:
        logger.error(f"Failed to send email: {e}")
        return False
