from app.llm.ollama_client import llm

response = llm.invoke("Who are you?")

print(response.content)