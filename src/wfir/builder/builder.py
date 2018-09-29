import wfir.builder.helper as helper


class Constants(object):
    SQL_QUERY_TASK_TYPE = "sql_query"


def sql_query(file_path, **kwargs):
    task = helper.create_task(type=Constants.SQL_QUERY_TASK_TYPE,
                              file_path=file_path,
                              **kwargs)
    return task
