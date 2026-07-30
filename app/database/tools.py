from sqlalchemy import inspect
from sqlalchemy.exc import SQLAlchemyError

from app.database.connection import engine
from app.database.executor import execute_query


def list_tables():
    """
    Returns all table names.
    """
    try:
        inspector = inspect(engine)
        return inspector.get_table_names()

    except SQLAlchemyError as e:
        return {
            "error": f"Database error while listing tables: {str(e)}"
        }


def describe_table(table_name: str):
    """
    Returns column information for a table.
    """
    try:
        inspector = inspect(engine)

        tables = inspector.get_table_names()

        if table_name not in tables:
            return {
                "error": f"Table '{table_name}' does not exist."
            }

        columns = inspector.get_columns(table_name)

        return [
            {
                "name": column["name"],
                "type": str(column["type"]),
            }
            for column in columns
        ]

    except SQLAlchemyError as e:
        return {
            "error": f"Database error: {str(e)}"
        }


def run_sql(sql: str):
    """
    Execute SQL safely.
    """
    try:
        return execute_query(sql)

    except SQLAlchemyError as e:
        return {
            "error": f"Database error: {str(e)}"
        }

    except Exception as e:
        return {
            "error": str(e)
        }