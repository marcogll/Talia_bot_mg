# app/llm.py
import openai
from config import OPENAI_API_KEY

def get_smart_response(prompt):
    """
    Generates a smart response using the OpenAI API.
    """
    if not OPENAI_API_KEY:
        return "Error: OpenAI API key is not configured."

    try:
        client = openai.OpenAI(api_key=OPENAI_API_KEY)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"An error occurred while communicating with OpenAI: {e}"
