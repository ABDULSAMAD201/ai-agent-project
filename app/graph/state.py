from typing import TypedDict, List


class GraphState(TypedDict):
    message: str
    response: str
    intent: str
    history: List[str]