from app.tools.sql_tools import (
    explain_sql,
    generate_sql,
    optimize_sql,
    detect_sql_bug,
)

print("=" * 50)
print(explain_sql.invoke({"query": "SELECT * FROM employees"}))

print("=" * 50)
print(generate_sql.invoke({"request": "Show all employees"}))

print("=" * 50)
print(optimize_sql.invoke({"query": "SELECT * FROM employees"}))

print("=" * 50)
print(detect_sql_bug.invoke({"query": "SELEC * FROM employees"}))