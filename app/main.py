from fastapi import FastAPI

from app.api.chat import router as chat_router
from app.core.config import APP_NAME

app = FastAPI(title=APP_NAME)

app.include_router(chat_router)


@app.get("/")
def home():
    return {
        "message": "AI Agent is running!"
    }