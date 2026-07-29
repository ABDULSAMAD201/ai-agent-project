from typing import Optional, Any

from pydantic import BaseModel


class ChatRequest(BaseModel):
    message: str
    session_id: Optional[str] = "default"


class ChatResponse(BaseModel):
    message: str
    sql: str | None = None
    results: list[dict[str, Any]] | None = None