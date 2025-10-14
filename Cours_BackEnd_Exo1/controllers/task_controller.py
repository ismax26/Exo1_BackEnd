from model.task import Task

class TaskController:
    """Gère les opérations sur les tâches (ajout, suppression, etc.)."""

    def __init__(self):
        self.tasks = []

    def add_task(self, title, description="", due_date=None):
        task = Task(title, description, due_date)
        self.tasks.append(task)
        return task

    def list_tasks(self):
        return self.tasks

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
            return True
        return False

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            return True
        return False
