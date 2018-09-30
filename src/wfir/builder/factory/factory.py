def create_task(**kwargs):
    from wfir.builder.factory.task import Task
    task = Task(**kwargs)
    return task
