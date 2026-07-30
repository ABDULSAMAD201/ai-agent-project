from typing import Any

from pydantic import BaseModel


class ChatRequest(BaseModel):
    message: str
    session_id: str = "default"


class ChatResponse(BaseModel):
    message: str
    tool_used: str | None = None
    sql: str | None = None
    results: list[dict[str, Any]] | None = None