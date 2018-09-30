import pytest
import wfir


@pytest.fixture()
def mock_create_task(mocker):
    yield mocker.patch("wfir.factory.create_task", auto_spec=True)


def test_sql_query(mocker, mock_create_task):
    # GIVEN
    sql_query_file_path = "path/to/sql_query/file.sql"
    compute = "compute"

    wfir_result = mocker.sentinel.wfir_result

    mock_create_task.return_value = wfir_result

    expected_result = wfir_result

    # WHEN
    actual_result = wfir.sql_query(sql_query_file_path, compute=compute)

    # THEN
    mock_create_task.assert_called_with(type="sql_query", file_path=sql_query_file_path, compute=compute)
    assert expected_result == actual_result


def test_input():
    # GIVEN
    pass