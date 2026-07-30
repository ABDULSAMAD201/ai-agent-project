from typing import Annotated
from typing_extensions import TypedDict

from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages


class GraphState(TypedDict):
    message: str
    response: str
    intent: str

    messages: Annotated[list[BaseMessage], add_messages]

    sql: str
    query_results: list[dict]

    tool_used: str