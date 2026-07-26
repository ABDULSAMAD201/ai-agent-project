from app.prompts.system_prompt import SYSTEM_PROMPT


def build_prompt(task_prompt: str) -> str:
    return f"""{SYSTEM_PROMPT}

{task_prompt}
"""