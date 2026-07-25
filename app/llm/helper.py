from langchain_core.messages import HumanMessage, SystemMessage

from app.llm.ollama_client import llm


def invoke_llm(system_prompt: str, user_message: str):

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_message),
    ]

    result = llm.invoke(messages)

    return result.content