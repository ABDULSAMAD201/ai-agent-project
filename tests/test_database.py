from app.database.tools import (
    list_tables,
    describe_table,
    run_sql,
)


def test_list_tables():
    tables = list_tables()

    assert isinstance(tables, list)
    assert "employees" in tables


def test_describe_table():
    columns = describe_table("employees")

    assert isinstance(columns, list)
    assert len(columns) > 0

    assert columns[0]["name"] == "id"


def test_run_sql():
    rows = run_sql("SELECT * FROM employees")

    assert isinstance(rows, list)