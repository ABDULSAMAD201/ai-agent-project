import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

APP_NAME = os.getenv("APP_NAME", "AI Agent Project")
HOST = os.getenv("HOST", "127.0.0.1")
PORT = int(os.getenv("PORT", 8000))
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2")