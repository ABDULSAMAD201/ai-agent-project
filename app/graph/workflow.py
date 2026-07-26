from langgraph.graph import START, END, StateGraph
from langgraph.checkpoint.memory import MemorySaver
from app.graph.state import GraphState
from app.graph.router import detect_intent

from app.graph.nodes import (
    explain_sql,
    detect_sql_bug,
    optimize_sql,
    generate_sql,
)

graph = StateGraph(GraphState)

# Register nodes
graph.add_node("intent_router", detect_intent)
graph.add_node("explain_sql", explain_sql)
graph.add_node("detect_sql_bug", detect_sql_bug)
graph.add_node("optimize_sql", optimize_sql)
graph.add_node("generate_sql", generate_sql)


graph.add_edge(START, "intent_router")


def route_intent(state: GraphState):
    return state["intent"]


graph.add_conditional_edges(
    "intent_router",
    route_intent,
    {
    "explain": "explain_sql",
    "bug_detection": "detect_sql_bug",
    "optimization": "optimize_sql",
    "generation": "generate_sql",

    },
)

graph.add_edge("explain_sql", END)
graph.add_edge("detect_sql_bug", END)
graph.add_edge("optimize_sql", END)
graph.add_edge("generate_sql", END)

memory = MemorySaver()

workflow = graph.compile(
    checkpointer=memory
)