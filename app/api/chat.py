from fastapi import APIRouter

from app.graph.workflow import workflow
from app.models.schemas import ChatRequest, ChatResponse

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    result = workflow.invoke(
        {
            "message": request.message,
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