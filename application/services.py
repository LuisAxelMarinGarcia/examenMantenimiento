from domain.entities import Task

class TaskService:
    def __init__(self, repository):
        self.repository = repository

    def create_task(self, title, description):
        new_task = Task(id=None, title=title, description=description)
        return self.repository.add(new_task)

    def get_task(self, task_id):
        return self.repository.get(task_id)

    def update_task(self, task_id, title, description, status):
        task = Task(id=task_id, title=title, description=description, status=status)
        return self.repository.update(task)

    def delete_task(self, task_id):
        return self.repository.delete(task_id)

    def list_tasks(self):
        return self.repository.list()
