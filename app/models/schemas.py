from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    message: str = Field(
        ...,
        description="User's SQL question or prompt",
        examples=["Explain this SQL query"],
    )


class ChatResponse(BaseModel):
    response: str = Field(
        ...,
        description="AI-generated response",
    )