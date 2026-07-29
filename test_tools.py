from app.database.tools import (
    list_tables,
    describe_table,
    run_sql,
)

print("Tables:")
print(list_tables())

print("\nEmployees schema:")
print(describe_table("employees"))

print("\nProjects schema:")
print(describe_table("projects"))

print("\nSQL execution:")
print(
    run_sql(
        """
        SELECT name, salary
        FROM employees;
        """
    )
)