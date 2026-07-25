from app.graph.state import GraphState


def detect_intent(state: GraphState):
    message = state["message"].lower()

    bug_keywords = [
        "bug",
        "bugs",
        "error",
        "errors",
        "fix",
        "issue",
        "issues",
        "wrong",
        "syntax",
    ]

    optimization_keywords = [
        "optimize",
        "optimization",
        "performance",
        "faster",
        "efficient",
        "improve",
    ]

    generation_keywords = [
        "show",
        "list",
        "find",
        "display",
        "get",
        "retrieve",
        "create query",
        "generate sql",
    ]

    if any(keyword in message for keyword in bug_keywords):
        return {"intent": "bug_detection"}

    if any(keyword in message for keyword in optimization_keywords):
        return {"intent": "optimization"}

    if any(keyword in message for keyword in generation_keywords):
        return {"intent": "generation"}

    return {"intent": "explain"}