from typing import TypedDict

from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.graph import END, START, StateGraph

from app.llm.ollama_client import llm
from app.prompts.sql_prompt import SQL_SYSTEM_PROMPT


class GraphState(TypedDict):
    message: str
    response: str


def sql_agent(state: GraphState):

    messages = [
        SystemMessage(content=SQL_SYSTEM_PROMPT),
        HumanMessage(content=state["message"]),
    ]

    result = llm.invoke(messages)

    return {
        "response": result.content
    }


graph = StateGraph(GraphState)

graph.add_node("sql_agent", sql_agent)

graph.add_edge(START, "sql_agent")
graph.add_edge("sql_agent", END)

workflow = graph.compile()