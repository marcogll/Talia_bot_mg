# talia_bot/modules/transcription.py
import logging
import openai
from talia_bot.config import OPENAI_API_KEY

logger = logging.getLogger(__name__)

async def transcribe_audio(audio_file) -> str | None:
    """
    Transcribes an audio file using OpenAI's Whisper model with the modern API call.

    Args:
        audio_file: A file-like object containing the audio data with a 'name' attribute.

    Returns:
        The transcribed text as a string, or None if transcription fails.
    """
    if not OPENAI_API_KEY:
        logger.error("Cannot transcribe audio: OPENAI_API_KEY is not configured.")
        return None

    try:
        client = openai.AsyncOpenAI(api_key=OPENAI_API_KEY)

        transcription = await client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )

        logger.info("Successfully transcribed audio.")
        return transcription.text
    except openai.APIError as e:
        logger.error(f"OpenAI API error during transcription: {e}")
        return None
    except Exception as e:
        logger.error(f"An unexpected error occurred during transcription: {e}")
        return None
