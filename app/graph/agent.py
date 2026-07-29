from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode

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
You are an intelligent SQL Assistant.

You have access to several tools.

Follow these rules:

1. If the user asks to CREATE SQL, use the SQL generation tool.

2. If the user asks to EXPLAIN SQL, use the SQL explanation tool.

3. If the user asks to OPTIMIZE SQL, use the SQL optimization tool.

4. If the user asks to FIX SQL, use the SQL bug detection tool.

5. If the user asks for DATA from the database:

- First generate the SQL.
- Then execute the SQL.
- Return the results.

6. If the user asks about tables or schema,
use the schema tools.

Always use tools instead of making up database information.
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

    print("=" * 50)
    print(response)
    print("=" * 50)

    return {
        "messages": [response],
        "response": response.content,
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