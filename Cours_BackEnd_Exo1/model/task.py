class Task:
    """Classe représentant une tâche à faire."""

    def __init__(self, title: str):
        self.title = title

    def __str__(self):
        return f"📝 {self.title}"
