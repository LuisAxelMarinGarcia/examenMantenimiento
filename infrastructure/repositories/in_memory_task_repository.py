from typing import List, Optional
from domain.entities import Task
from domain.ports import TaskRepositoryPort

class InMemoryTaskRepository(TaskRepositoryPort):

    def __init__(self):
        self.tasks = {}
        self.current_id = 0

    def add(self, task: Task) -> Task:
        self.current_id += 1
        task.id = self.current_id
        self.tasks[self.current_id] = task
        return task

    def get(self, task_id: int) -> Optional[Task]:
        return self.tasks.get(task_id)

    def update(self, task: Task) -> Optional[Task]:
        if task.id in self.tasks:
            self.tasks[task.id] = task
            return task
        return None

    def delete(self, task_id: int) -> bool:
        if task_id in self.tasks:
            del self.tasks[task_id]
            return True
        return False

    def list(self) -> List[Task]:
        return list(self.tasks.values())
