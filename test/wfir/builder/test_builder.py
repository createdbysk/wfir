import pytest
from wfir import builder


@pytest.fixture()
def mock_create_task(mocker):
    yield mocker.patch("wfir.builder.helper.create_task", auto_spec=True)


def test_sql_query(mocker, mock_create_task):
    # GIVEN
    sql_query_file_path = "path/to/sql_query/file.sql"
    compute = "compute"

    builder_result = mocker.sentinel.builder_result

    mock_create_task.return_value = builder_result

    expected_result = builder_result

    # WHEN
    actual_result = builder.sql_query(sql_query_file_path, compute=compute)

    # THEN
    mock_create_task.assert_called_with(type="sql_query", file_path=sql_query_file_path, compute=compute)
    assert expected_result == actual_result
