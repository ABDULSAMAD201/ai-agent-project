conversation_memory = {}


def get_history(session_id: str):
    return conversation_memory.get(session_id, [])


def save_message(session_id: str, message: str):
    history = conversation_memory.setdefault(session_id, [])
    history.append(message)