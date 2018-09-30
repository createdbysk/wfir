def create_task(**kwargs):
    from wfir.factory.task import Task
    task = Task(**kwargs)
    return task
