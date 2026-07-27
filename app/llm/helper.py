from langchain_core.messages import (
    HumanMessage,
    SystemMessage,
    BaseMessage,
)

from app.llm.ollama_client import llm
from app.prompts.prompt_builder import build_prompt


def invoke_llm(
    task_prompt: str,
    user_message: str,
    history: list[BaseMessage] | None = None,
):

    messages = [
        SystemMessage(content=build_prompt(task_prompt)),
    ]

    if history:
        messages.extend(history)

    messages.append(HumanMessage(content=user_message))

    result = llm.invoke(messages)

    return result.content