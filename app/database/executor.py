from sqlalchemy import text

from app.database.connection import SessionLocal


def execute_query(sql: str):
    """
    Execute a read-only SQL query and return the results.
    """

    sql = sql.strip()

    # Safety check
    if not (
        sql.lower().startswith("select")
        or sql.lower().startswith("with")
    ):
        raise ValueError("Only SELECT queries are allowed.")

    db = SessionLocal()

    try:
        result = db.execute(text(sql))

        rows = result.mappings().all()

        return [dict(row) for row in rows]

    finally:
        db.close()