from langchain_core.tools import tool

from app.llm.helper import invoke_llm

from app.prompts.sql_generator import SQL_GENERATOR_PROMPT
from app.prompts.sql_explainer import SQL_EXPLAINER_PROMPT
from app.prompts.sql_optimizer import SQL_OPTIMIZER_PROMPT
from app.prompts.sql_bug_detector import SQL_BUG_DETECTOR_PROMPT

@tool
def explain_sql(query: str) -> str:
    """
    Explain an SQL query in simple language.
    """

    return invoke_llm(
        SQL_EXPLAINER_PROMPT,
        query,
    )

@tool
def generate_sql(request: str) -> str:
    """
    Generate an SQL query from a natural language request.
    """

    return invoke_llm(
        SQL_GENERATOR_PROMPT,
        request,
    )

@tool
def optimize_sql(query: str) -> str:
    """
    Optimize an SQL query for better performance.
    """

    return invoke_llm(
        SQL_OPTIMIZER_PROMPT,
        query,
    )

@tool
def detect_sql_bug(query: str) -> str:
    """
    Find bugs or syntax errors in an SQL query.
    """

    return invoke_llm(
        SQL_BUG_DETECTOR_PROMPT,
        query,
    )