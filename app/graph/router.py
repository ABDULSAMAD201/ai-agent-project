from app.graph.state import GraphState


def detect_intent(state: GraphState):
    message = state["message"].lower()

    history = state.get("messages", [])

    last_ai_response = ""

    if history:
        for msg in reversed(history):
            if hasattr(msg, "content"):
                last_ai_response = msg.content.lower()
                break

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
        "generate",
        "create",
        "write",
        "show",
        "list",
        "find",
        "display",
        "retrieve",
        "select",
    ]

    if any(keyword in message for keyword in bug_keywords):
        return {"intent": "bug_detection"}

    if any(keyword in message for keyword in optimization_keywords):
        return {"intent": "optimization"}

    if any(keyword in message for keyword in generation_keywords):
        return {"intent": "generation"}

    if "optimize it" in message and "select" in last_ai_response:
        return {"intent": "optimization"}

    if "explain it" in message and "select" in last_ai_response:
        return {"intent": "explain"}

    if "fix it" in message and "select" in last_ai_response:
        return {"intent": "bug_detection"}

    return {"intent": "explain"}