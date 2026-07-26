from app.prompts.sql_generator import SQL_GENERATOR_PROMPT
from app.graph.state import GraphState
from langgraph.graph import END, START, StateGraph
from app.llm.helper import invoke_llm

from app.prompts.sql_explainer import SQL_EXPLAINER_PROMPT
from app.prompts.sql_bug_detector import SQL_BUG_DETECTOR_PROMPT
from app.prompts.sql_optimizer import SQL_OPTIMIZER_PROMPT
from app.prompts.sql_generator import SQL_GENERATOR_PROMPT
    

def explain_sql(state: GraphState):

    response = invoke_llm(
        SQL_EXPLAINER_PROMPT,
        state["message"]
    )
    

    return {
        "response": response
    }

def detect_sql_bug(state: GraphState):

    response = invoke_llm(
        SQL_BUG_DETECTOR_PROMPT,
        state["message"]
    )

    return {
        "response": response
    }

def optimize_sql(state: GraphState):

    response = invoke_llm(
        SQL_OPTIMIZER_PROMPT,
        state["message"]
    )

    return {
        "response": response
    }

def generate_sql(state: GraphState):

    response = invoke_llm(
        SQL_GENERATOR_PROMPT,
        state["message"]
    )

    return {
        "response": response
    }