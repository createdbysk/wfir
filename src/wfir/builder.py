import wfir.factory as factory


class Constants(object):
    SQL_QUERY_TASK_TYPE = "sql_query"


def sql_query(file_path, **kwargs):
    task = factory.create_task(type=Constants.SQL_QUERY_TASK_TYPE,
                               file_path=file_path,
                               **kwargs)
    return task
