import wfir.fields


class Constants(object):
    SQL_QUERY_TASK_TYPE = "sql_query"


def sql_query(file_path, **kwargs):
    ir = kwargs.copy()
    ir[wfir.fields.TYPE_KEY] = Constants.SQL_QUERY_TASK_TYPE
    ir[wfir.fields.FILE_PATH_KEY] = file_path
    return ir
