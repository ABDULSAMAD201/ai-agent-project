from typing import Any

from pydantic import BaseModel


class ChatRequest(BaseModel):
    session_id: str
    message: str


class ChatResponse(BaseModel):
    message: str
    sql: str | None = None
    results: list[dict[str, Any]] | None = None