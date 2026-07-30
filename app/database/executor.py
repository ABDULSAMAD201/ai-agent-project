from sqlalchemy import text

from app.core.logger import logger
from app.database.connection import SessionLocal


def execute_query(sql: str):
    """
    Execute a read-only SQL query safely and return the results.
    """

    # Remove whitespace and trailing semicolons
    sql = sql.strip().rstrip(";")
    sql_lower = sql.lower()

    # Block dangerous SQL keywords
    dangerous_keywords = [
        "drop",
        "delete",
        "update",
        "insert",
        "alter",
        "truncate",
        "create",
        "replace",
    ]

    for keyword in dangerous_keywords:
        if keyword in sql_lower:
            logger.warning(
                f"Blocked unsafe SQL query containing '{keyword.upper()}': {sql}"
            )
            raise ValueError(
                f"Unsafe SQL detected: '{keyword.upper()}' statements are not allowed."
            )

    # Allow only SELECT and WITH queries
    if not (
        sql_lower.startswith("select")
        or sql_lower.startswith("with")
    ):
        logger.warning(f"Blocked non-SELECT SQL query: {sql}")
        raise ValueError("Only SELECT queries are allowed.")

    db = SessionLocal()

    try:
        logger.info(f"Executing SQL: {sql}")

        result = db.execute(text(sql))
        rows = result.mappings().all()

        logger.info(f"Query executed successfully. Returned {len(rows)} row(s).")

        return [dict(row) for row in rows]

    except Exception as e:
        logger.error(f"SQL execution failed: {str(e)}")
        raise ValueError(f"SQL execution failed: {str(e)}")

    finally:
        db.close()