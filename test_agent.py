from app.graph.agent import agent

result = agent.invoke(
    {
        "message": "Find the bug in: SELEC * FROM employees",
        "messages": [],
    }
)

print(result)