class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def delete_task(self, task_index):
        del self.tasks[task_index]

    def mark_completed(self, task_index):
        self.tasks[task_index]["completed"] = True

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            for index, task in enumerate(self.tasks):
                status = "Completed" if task["completed"] else "Not Completed"
                print(f"{index + 1}. {task['task']} - {status}")

def main():
    todo_list = TodoList()

    while True:
        print("\nTODO LIST MENU:")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Mark Task as Completed")
        print("4. Display Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            todo_list.add_task(task)
            print("Task added successfully.")
        elif choice == "2":
            if not todo_list.tasks:
                print("No tasks in the list.")
            else:
                task_index = int(input("Enter task number to delete: ")) - 1
                todo_list.delete_task(task_index)
                print("Task deleted successfully.")
        elif choice == "3":
            if not todo_list.tasks:
                print("No tasks in the list.")
            else:
                task_index = int(input("Enter task number to mark as completed: ")) - 1
                todo_list.mark_completed(task_index)
                print("Task marked as completed.")
        elif choice == "4":
            todo_list.display_tasks()
        elif choice == "5":
            print("Exiting the program. Goodbye!!!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
