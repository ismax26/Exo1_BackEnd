from datetime import datetime
from typing import Optional

class Task:
    """Représente une tâche à faire."""

    def __init__(self, title: str, description: str = "", due_date: Optional[str] = None):
        self.title = title
        self.description = description
        self.completed = False
        self.created_at = datetime.now()
        self.due_date = due_date

    def mark_completed(self):
        """Marque la tâche comme complétée."""
        self.completed = True

    def __str__(self):
        status = "✅" if self.completed else "🕓"
        due = f" | Échéance: {self.due_date}" if self.due_date else ""
        return f"{status} {self.title}{due} - {self.description}"
