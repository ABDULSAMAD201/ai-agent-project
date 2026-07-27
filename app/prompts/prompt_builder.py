from app.database.schema import get_database_schema
from app.prompts.system_prompt import SYSTEM_PROMPT


def build_prompt(task_prompt: str) -> str:

    schema = get_database_schema()

    return f"""
{SYSTEM_PROMPT}

Database Schema:

{schema}

Task:

{task_prompt}
"""