from app.database.executor import execute_query

query = """
WITH high_salary AS (
    SELECT *
    FROM employees
    WHERE salary > 70000
)

SELECT *
FROM high_salary;
"""

results = execute_query(query)

print(results)