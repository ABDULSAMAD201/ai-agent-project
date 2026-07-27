from langchain_core.messages import AIMessage, HumanMessage
from app.database.executor import execute_query
from app.graph.state import GraphState
from app.llm.helper import invoke_llm
from app.prompts.sql_bug_detector import SQL_BUG_DETECTOR_PROMPT
from app.prompts.sql_explainer import SQL_EXPLAINER_PROMPT
from app.prompts.sql_generator import SQL_GENERATOR_PROMPT
from app.prompts.sql_optimizer import SQL_OPTIMIZER_PROMPT    

def explain_sql(state: GraphState):

    response = invoke_llm(
        SQL_EXPLAINER_PROMPT,
        state["message"],
        state.get("messages", [])
    )
    

    return {
        "response": response,
        "messages": [
            HumanMessage(content=state["message"]),
            AIMessage(content=response),
        ],
    }

def detect_sql_bug(state: GraphState):

    response = invoke_llm(
        SQL_BUG_DETECTOR_PROMPT,
        state["message"],
        state.get("messages", [])
    )

    return {
        "response": response,
        "messages": [
            HumanMessage(content=state["message"]),
            AIMessage(content=response),
        ],
    }


def optimize_sql(state: GraphState):

    response = invoke_llm(
        SQL_OPTIMIZER_PROMPT,
        state["message"],
        state.get("messages", [])
    )

    return {
        "response": response,
        "messages": [
            HumanMessage(content=state["message"]),
            AIMessage(content=response),
        ],
    }


def generate_sql(state: GraphState):
    """
    Generate SQL and execute it against the database.
    """

    sql = invoke_llm(
        SQL_GENERATOR_PROMPT,
        state["message"],
        state.get("messages", []),
    )

    try:
        results = execute_query(sql)

        response = (
            f"Generated SQL:\n\n{sql}\n\n"
            f"Results:\n{results}"
        )

        return {
            "response": "Query executed successfully.",
            "sql": sql,
            "query_results": results,
            "messages": [
                HumanMessage(content=state["message"]),
                AIMessage(content=response),
            ],
        }

    except Exception as e:

        response = str(e)

        return {
            "response": response,
            "sql": sql,
            "query_results": [],
            "messages": [
                HumanMessage(content=state["message"]),
                AIMessage(content=response),
            ],
        }
