# bot/modules/file_validation.py
# This module provides functions for validating files before processing.

import logging
from telegram import Document

# Set up logging
logger = logging.getLogger(__name__)

# --- Configuration ---
# Whitelist of allowed MIME types. Prevents processing of potentially harmful files.
# Examples: 'application/pdf', 'image/jpeg', 'application/msword',
# 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
ALLOWED_MIME_TYPES = {
    'application/pdf',
    'application/msword',
    'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    'text/plain',
    'image/jpeg',
    'image/png'
}

# Maximum file size in bytes (e.g., 10 * 1024 * 1024 for 10 MB)
MAX_FILE_SIZE_BYTES = 10 * 1024 * 1024  # 10 MB

# --- Validation Functions ---

def is_file_type_allowed(document: Document) -> bool:
    """
    Checks if the document's MIME type is in the allowed whitelist.

    Args:
        document: The Telegram Document object to check.

    Returns:
        True if the MIME type is allowed, False otherwise.
    """
    if not document or not document.mime_type:
        logger.warning("Document or its MIME type is missing.")
        return False

    logger.info(f"Validating file type: {document.mime_type}")

    if document.mime_type in ALLOWED_MIME_TYPES:
        logger.info("File type is allowed.")
        return True
    else:
        logger.warning(f"File type '{document.mime_type}' is not in the allowed list.")
        return False

def is_file_size_acceptable(document: Document) -> bool:
    """
    Checks if the document's file size is within the acceptable limit.

    Args:
        document: The Telegram Document object to check.

    Returns:
        True if the file size is acceptable, False otherwise.
    """
    if not document or document.file_size is None:
        logger.warning("Document or its file size is missing.")
        return False

    logger.info(f"Validating file size: {document.file_size} bytes.")

    if document.file_size <= MAX_FILE_SIZE_BYTES:
        logger.info("File size is acceptable.")
        return True
    else:
        logger.warning(f"File size {document.file_size} exceeds the limit of {MAX_FILE_SIZE_BYTES} bytes.")
        return False

def validate_document(document: Document) -> (bool, str):
    """
    Performs all validation checks on a document.

    Args:
        document: The Telegram Document object to validate.

    Returns:
        A tuple containing a boolean indicating if the document is valid,
        and a string message explaining the result.
    """
    if not is_file_type_allowed(document):
        return False, f"Unsupported file type: {document.mime_type}. Please upload a supported document."

    if not is_file_size_acceptable(document):
        return False, f"File is too large. The maximum allowed size is {MAX_FILE_SIZE_BYTES // 1024 // 1024} MB."

    return True, "File is valid and can be processed."
