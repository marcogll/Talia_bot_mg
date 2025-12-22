# bot/modules/transcription.py
# This module handles audio transcription using the Whisper API.

import logging
import os
from openai import OpenAI
from bot.config import OPENAI_API_KEY

# Set up logging
logger = logging.getLogger(__name__)

# Initialize the OpenAI client
if not OPENAI_API_KEY:
    logger.error("OPENAI_API_KEY is not configured in environment variables.")
    client = None
else:
    client = OpenAI(api_key=OPENAI_API_KEY)

def transcribe_audio(file_path: str) -> str:
    """
    Transcribes an audio file using the Whisper API.

    Args:
        file_path: The path to the audio file to transcribe.

    Returns:
        The transcribed text, or an error message if transcription fails.
    """
    if not client:
        return "Error: OpenAI API key is not configured."

    if not os.path.exists(file_path):
        logger.error(f"Audio file not found at: {file_path}")
        return "Error: Audio file not found."

    try:
        logger.info(f"Transcribing audio from: {file_path}")
        with open(file_path, "rb") as audio_file:
            transcript = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file
            )
        logger.info("Transcription successful.")
        return transcript.text
    except Exception as e:
        logger.error(f"Error during audio transcription: {e}")
        return "Error: Could not transcribe audio."
