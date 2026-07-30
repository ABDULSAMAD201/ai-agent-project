from app.tools.database_tools import (
    list_database_tables,
    describe_database_table,
    execute_sql,
)


def test_list_database_tables():
    result = list_database_tables.invoke({})

    assert isinstance(result, list)


def test_describe_database_table():
    result = describe_database_table.invoke(
        {
            "table_name": "employees"
        }
    )

    assert isinstance(result, list)


def test_execute_sql():
    result = execute_sql.invoke(
        {
            "sql": "SELECT * FROM employees"
        }
    )

    assert isinstance(result, list)