from model.task import Task

class TaskController:
    """Gère la logique métier : ajout, suppression, affichage des tâches."""

    def __init__(self):
        self.tasks = []  # Liste pour stocker les tâches

    def add_task(self, title):
        """Ajoute une nouvelle tâche à la liste."""
        task = Task(title)
        self.tasks.append(task)
        return task

    def list_tasks(self):
        """Retourne la liste des tâches."""
        return self.tasks

    def delete_task(self, index):
        """Supprime une tâche selon son index."""
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            return True
        return False
