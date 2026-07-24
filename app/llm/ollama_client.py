from langchain_ollama import ChatOllama

from app.core.config import OLLAMA_MODEL

llm = ChatOllama(
    model=OLLAMA_MODEL,
    temperature=0
)