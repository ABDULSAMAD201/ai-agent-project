from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode
from app.core.logger import logger
from app.graph.state import GraphState
from app.llm.ollama_client import llm

from app.tools.sql_tools import (
    explain_sql,
    generate_sql,
    optimize_sql,
    detect_sql_bug,
)

from app.tools.database_tools import (
    list_database_tables,
    describe_database_table,
    execute_sql,
)

# -----------------------------
# Tools
# -----------------------------
tools = [
    # Database tools
    list_database_tables,
    describe_database_table,
    execute_sql,

    # SQL tools
    explain_sql,
    generate_sql,
    optimize_sql,
    detect_sql_bug,
]

tool_node = ToolNode(tools)

# -----------------------------
# Graph
# -----------------------------
graph = StateGraph(GraphState)


def agent_node(state: GraphState):

    messages = [
        SystemMessage(
            content="""
You are an AI SQL Assistant.

You have access to tools that interact with a database.

IMPORTANT:
- Do not ask the user to choose an option if their request is already clear.
- If a suitable tool exists, call it immediately.
- Never answer questions about the database from memory.
- Always use the available tools.

Use these rules:

1. If the user asks to list tables, call list_database_tables.

2. If the user asks to describe a table, call describe_database_table.

3. If the user asks to generate SQL, call generate_sql.

4. If the user asks to explain SQL, call explain_sql.

5. If the user asks to optimize SQL, call optimize_sql.

6. If the user asks to find bugs in SQL, call detect_sql_bug.

7. If the user provides an SQL query and asks to execute it,
call execute_sql.

Always prefer calling a tool over responding conversationally.
"""
        )
    ]

    # First user message
    if not state.get("messages"):
        messages.append(HumanMessage(content=state["message"]))
    else:
        # Continue the conversation after tool execution
        messages.extend(state["messages"])

    llm_with_tools = llm.bind_tools(tools)

    response = llm_with_tools.invoke(messages)

    logger.info("LLM Response:")
    logger.info(response)

    tool_name = None

    if response.tool_calls:
        tool_name = response.tool_calls[0]["name"]

    return {
        "messages": [response],
        "response": response.content,
        "tool_used": tool_name,
    }

def should_continue(state: GraphState):

    messages = state["messages"]

    last_message = messages[-1]

    if last_message.tool_calls:
        return "tools"

    return END


# -----------------------------
# Nodes
# -----------------------------
graph.add_node("agent", agent_node)
graph.add_node("tools", tool_node)

# -----------------------------
# Edges
# -----------------------------
graph.add_edge(START, "agent")

graph.add_conditional_edges(
    "agent",
    should_continue,
)

graph.add_edge("tools", "agent")

# -----------------------------
# Compile
# -----------------------------
agent = graph.compile()