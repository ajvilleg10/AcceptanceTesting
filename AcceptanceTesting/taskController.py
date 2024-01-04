from task import Task


class TaskController:
    def __init__(self):
        self._tasks = []

    def add_task(self, description, due_date, priority):
        task = Task(description, due_date, priority)
        self._tasks.append(task)

    def list_tasks(self):
        if not self._tasks:
            print("No tasks found.")
        else:
            for index, task in enumerate(self._tasks, start=1):
                status = "Completed" if task.completed else "Pending"
                print(f"{index}. [{status}] {task.description} (Due: {task.due_date}, Priority: {task.priority})")

    def mark_completed(self, task_index):
        if 0 < task_index <= len(self._tasks):
            task = self._tasks[task_index - 1]
            task.completed = True
        else:
            print("Invalid task index.")

    def clear_tasks(self):
        self._tasks = []

    def sort_tasks_by_priority(self):
        self._tasks.sort(key=lambda task: task.priority)