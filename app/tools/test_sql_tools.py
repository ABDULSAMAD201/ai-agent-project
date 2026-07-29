from app.tools.sql_tools import explain_sql

print(
    explain_sql.invoke(
        {
            "query": "SELECT * FROM employees"
        }
    )
)