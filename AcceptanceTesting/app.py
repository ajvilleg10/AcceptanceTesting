from taskController import TaskController

class ToDoListApp:
    def __init__(self):
        self._controller = TaskController()

    def run(self):
        while True:
            print("\nTo-Do List Manager")
            print("1. Add Task")
            print("2. List Tasks")
            print("3. Mark Task as Completed")
            print("4. Clear All Tasks")
            print("5. Sort Tasks by Priority")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                description = input("Enter task description: ")
                due_date = input("Enter due date: ")
                priority = input("Enter priority: ")
                self._controller.add_task(description, due_date, priority)
                print("Task added successfully.")
            elif choice == "2":
                self._controller.list_tasks()
            elif choice == "3":
                try:
                    task_index = int(input("Enter task index to mark as completed: "))
                    self._controller.mark_completed(task_index)
                    print("Task marked as completed.")
                except ValueError:
                    print("Invalid task index. Please enter a valid number.")
            elif choice == "4":
                self._controller.clear_tasks()
                print("All tasks cleared.")
            elif choice == "5":
                self._controller.sort_tasks_by_priority()
                print("Tasks sorted by priority.")
            elif choice == "6":
                break
            else:
                print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    app = ToDoListApp()
    app.run()