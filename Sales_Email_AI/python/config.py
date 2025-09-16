# %%writefile config.py
import os
import logging
from pydantic import BaseModel
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class Settings(BaseModel):
    """
    Pydantic model for managing application settings.
    It automatically reads environment variables and validates their types.
    """
    # API Keys
    OPENAI_API_KEY: str = os.getenv('OPENAI_API_KEY')
    GOOGLE_GEMINI_API_KEY: str = os.getenv('GOOGLE_GEMINI_API_KEY')
    DEEPSEEK_API_KEY: str = os.getenv('DEEPSEEK_API_KEY')
    GROQ_API_KEY: str = os.getenv('GROQ_API_KEY')
    SENDGRID_API_KEY: str = os.getenv('SENDGRID_API_KEY')

    # Email Settings
    FROM_EMAIL: str = os.getenv('FROM_EMAIL')
    TO_EMAIL: str = os.getenv('TO_EMAIL')

    # API Base URLs
    GEMINI_BASE_URL: str = "https://generativelanguage.googleapis.com/v1beta/"
    DEEPSEEK_BASE_URL: str = "https://api.deepseek.com/v1"
    GROQ_BASE_URL: str = "https://api.groq.com/openai/v1"

# Create a single, globally accessible instance of the settings
try:
    settings = Settings()
    logging.info("Configuration loaded successfully.")
except ValueError as e:
    logging.error(f"Configuration error: {e}")
    raise
# %%
