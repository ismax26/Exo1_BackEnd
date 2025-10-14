import sys
import os

# Permet à Python de trouver les modules situés dans les autres dossiers
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from controllers.task_controller import TaskController


class CLI:
    """Interface en ligne de commande (le 'V' de MVC)."""

    def __init__(self):
        self.controller = TaskController()

    def display_menu(self):
        print("\n=== ToDoList CLI ===")
        print("1️⃣  Ajouter une tâche")
        print("2️⃣  Afficher la liste des tâches")
        print("3️⃣  Supprimer une tâche")
        print("4️⃣  Quitter")

    def run(self):
        """Boucle principale de l'application CLI."""
        while True:
            self.display_menu()
            choice = input("\nChoix : ")

            if choice == "1":
                title = input("Titre de la tâche : ")
                task = self.controller.add_task(title)
                print(f"Tâche ajoutée : {task}")

            elif choice == "2":
                tasks = self.controller.list_tasks()
                if not tasks:
                    print("Aucune tâche pour le moment.")
                else:
                    print("\n📋 Liste des tâches :")
                    for i, task in enumerate(tasks):
                        print(f"{i}. {task}")

            elif choice == "3":
                index = int(input("Numéro de la tâche à supprimer : "))
                if self.controller.delete_task(index):
                    print(" Tâche supprimée.")
                else:
                    print(" Numéro invalide.")

            elif choice == "4":
                print(" Au revoir !")
                break

            else:
                print("Choix invalide, réessayez.")
