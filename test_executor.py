from app.database.executor import execute_query

query = """
SELECT
    e.name,
    d.name AS department
FROM employees e
JOIN departments d
ON e.department_id = d.id;
"""

results = execute_query(query)

print(results)