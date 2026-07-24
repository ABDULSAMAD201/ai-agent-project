from app.graph.workflow import workflow

result = workflow.invoke(
    {
        "message": "Explain LangGraph in one sentence."
    }
)

print(result["response"])