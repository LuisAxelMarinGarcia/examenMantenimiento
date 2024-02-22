class InMemoryTaskRepository:
    def __init__(self):
        self.tasks = {}
        self.current_id = 0

    def add(self, task):
        self.current_id += 1
        task.id = self.current_id
        self.tasks[self.current_id] = task
        return task

    def get(self, task_id):
        return self.tasks.get(task_id)

    def update(self, task):
        if task.id in self.tasks:
            self.tasks[task.id] = task
            return task
        return None

    def delete(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]
            return True
        return False

    def list(self):
        return list(self.tasks.values())
