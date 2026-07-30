import pytest

from app.database.executor import execute_query


def test_allow_select():

    result = execute_query(
        "SELECT * FROM employees"
    )

    assert isinstance(result, list)


@pytest.mark.parametrize(
    "query",
    [
        "DROP TABLE employees",
        "DELETE FROM employees",
        "UPDATE employees SET salary=0",
        "INSERT INTO employees VALUES(1)",
        "ALTER TABLE employees ADD age INT",
    ],
)
def test_block_dangerous_queries(query):

    with pytest.raises(ValueError):
        execute_query(query)