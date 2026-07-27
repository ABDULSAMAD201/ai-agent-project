from sqlalchemy import inspect

from app.database.connection import engine


def get_database_schema() -> str:
    """
    Returns a formatted description of the database schema.
    """

    inspector = inspect(engine)

    schema = ""

    tables = inspector.get_table_names()

    for table in tables:
        schema += f"Table: {table}\n"

        columns = inspector.get_columns(table)

        for column in columns:
            schema += (
                f"  - {column['name']} "
                f"({column['type']})\n"
            )

        schema += "\n"

    return schema