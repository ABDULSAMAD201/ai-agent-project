from langchain_core.messages import HumanMessage, SystemMessage

from app.llm.ollama_client import llm
from app.prompts.intent_classifier import INTENT_CLASSIFIER_PROMPT


def classify_intent(message: str) -> str:

    messages = [
        SystemMessage(content=INTENT_CLASSIFIER_PROMPT),
        HumanMessage(content=message),
    ]

    response = llm.invoke(messages)

    return response.content.strip().lower()