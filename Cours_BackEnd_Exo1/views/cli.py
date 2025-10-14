import sys
import os

# Permet d'importer les modules depuis la racine du projet
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from controllers.task_controller import TaskController


class CLI:
    """Interface en ligne de commande pour la ToDoList."""

    def __init__(self):
        self.controller = TaskController()

    def display_menu(self):
        print("\n=== ToDoList CLI ===")
        print("1️⃣  Ajouter une tâche")
        print("2️⃣  Lister les tâches")
        print("3️⃣  Marquer une tâche comme terminée")
        print("4️⃣  Supprimer une tâche")
        print("5️⃣  Quitter")

    def run(self):
        while True:
            self.display_menu()
            choice = input("\nChoix : ")

            if choice == "1":
                title = input("Titre : ")
                description = input("Description : ")
                due_date = input("Date limite (optionnel) : ")
                task = self.controller.add_task(title, description, due_date)
                print(f"Tâche ajoutée : {task}")

            elif choice == "2":
                tasks = self.controller.list_tasks()
                if not tasks:
                    print("Aucune tâche pour le moment.")
                else:
                    for i, task in enumerate(tasks):
                        print(f"{i}. {task}")

            elif choice == "3":
                index = int(input("Numéro de la tâche à terminer : "))
                if self.controller.complete_task(index):
                    print(" Tâche complétée !")
                else:
                    print(" Tâche introuvable.")

            elif choice == "4":
                index = int(input("Numéro de la tâche à supprimer : "))
                if self.controller.delete_task(index):
                    print(" Tâche supprimée.")
                else:
                    print(" Tâche introuvable.")

            elif choice == "5":
                print(" Au revoir !")
                break

            else:
                print("Choix invalide, réessayez.")
