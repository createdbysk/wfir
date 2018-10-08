import wfir


def test_sql_query():
    # GIVEN
    sql_query_file_path = "path/to/sql_query/file.sql"
    compute = "compute"

    ir = {
        "type": "sql_query",
        "file_path": sql_query_file_path,
        "compute": compute
    }
    expected_result = ir

    # WHEN
    actual_result = wfir.sql_query(sql_query_file_path, compute=compute)

    # THEN
    assert expected_result == actual_result
