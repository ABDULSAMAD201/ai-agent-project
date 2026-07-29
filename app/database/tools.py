from sqlalchemy import inspect

from app.database.connection import engine
from app.database.executor import execute_query


def list_tables():
    """
    Returns all table names.
    """
    inspector = inspect(engine)
    return inspector.get_table_names()


def describe_table(table_name: str):
    """
    Returns column information for a table.
    """
    inspector = inspect(engine)

    columns = inspector.get_columns(table_name)

    return [
        {
            "name": column["name"],
            "type": str(column["type"]),
        }
        for column in columns
    ]


def run_sql(sql: str):
    """
    Execute SQL safely.
    """
    return execute_query(sql)