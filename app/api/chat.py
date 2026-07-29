from fastapi import APIRouter

from app.graph.agent import agent
from app.models.schemas import ChatRequest, ChatResponse

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

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
        sql=result.get("sql"),
        results=result.get("query_results"),
    )