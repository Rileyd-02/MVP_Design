import os
from dotenv import load_dotenv

load_dotenv()

def get_openai_key():
    """Load OpenAI API key from .env or environment variable."""
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        raise ValueError("OPENAI_API_KEY not set in environment.")
    return key