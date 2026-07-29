from langchain_core.tools import tool

from app.database.tools import (
    list_tables,
    describe_table,
    run_sql,
)

@tool
def list_database_tables():
    """
    Return all database tables.
    """
    return list_tables()

@tool
def describe_database_table(table_name: str):
    """
    Describe the columns of a database table.
    """
    return describe_table(table_name)

@tool
def execute_sql(sql: str):
    """
    Execute a SELECT SQL query.
    """
    return run_sql(sql)