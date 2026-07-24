from fastapi import FastAPI

from app.core.config import APP_NAME
from app.core.logger import logger

app = FastAPI(title=APP_NAME)


@app.get("/")
def home():
    logger.info("Home endpoint accessed")

    return {
        "message": "AI Agent Project Running!"
    }