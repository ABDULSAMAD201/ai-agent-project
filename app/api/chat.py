from fastapi import APIRouter

from app.core.logger import logger
from app.graph.agent import agent
from app.models.schemas import ChatRequest, ChatResponse

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    logger.info(f"User Prompt: {request.message}")
    logger.info(f"Session ID: {request.session_id}")

    result = agent.invoke(
        {
            "message": request.message,
            "messages": [],
        },
        config={
            "configurable": {
                "thread_id": request.session_id,
            }
        },
    )

    return ChatResponse(
        message=result["response"],
        tool_used=result.get("tool_used"),
        sql=result.get("sql"),
        results=result.get("query_results"),
    )