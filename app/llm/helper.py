from langchain_core.messages import HumanMessage, SystemMessage
from app.prompts.prompt_builder import build_prompt
from app.llm.ollama_client import llm


def invoke_llm(task_prompt: str, user_message: str):

    messages = [
        SystemMessage(content=build_prompt(task_prompt)),
        HumanMessage(content=user_message),
    ]

    result = llm.invoke(messages)

    return result.content