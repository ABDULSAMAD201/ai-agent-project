from app.tools.database_tools import (
    list_database_tables,
    describe_database_table,
    execute_sql,
)

print(list_database_tables.invoke({}))

print(
    describe_database_table.invoke(
        {"table_name": "employees"}
    )
)

print(
    execute_sql.invoke(
        {
            "sql": """
            SELECT *
            FROM employees;
            """
        }
    )
)