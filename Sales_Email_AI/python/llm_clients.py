# %%writefile llm_clients.py
from openai import AsyncOpenAI
from config import settings

# Initialize clients for each LLM provider
# This makes them reusable across the application
gemini_client = AsyncOpenAI(base_url=settings.GEMINI_BASE_URL, api_key=settings.GOOGLE_GEMINI_API_KEY)
groq_client = AsyncOpenAI(base_url=settings.GROQ_BASE_URL, api_key=settings.GROQ_API_KEY)
deepseek_client = AsyncOpenAI(base_url=settings.DEEPSEEK_BASE_URL, api_key=settings.DEEPSEEK_API_KEY)
openai_client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)