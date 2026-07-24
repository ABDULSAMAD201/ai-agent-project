from typing import TypedDict

from langgraph.graph import StateGraph, START, END

from app.llm.ollama_client import llm


class GraphState(TypedDict):
    message: str
    response: str


def chatbot(state: GraphState):
    result = llm.invoke(state["message"])

    return {
        "response": result.content
    }


graph = StateGraph(GraphState)

graph.add_node("chatbot", chatbot)

graph.add_edge(START, "chatbot")
graph.add_edge("chatbot", END)

workflow = graph.compile()