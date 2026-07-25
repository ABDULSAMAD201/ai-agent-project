from app.graph.workflow import workflow

result = workflow.invoke(
    {
        "message": """
Explain this SQL query:

SELECT *
FROM employees
WHERE salary > 50000;
"""
    }
)

print(result["response"])