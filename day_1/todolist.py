class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added to your to-do list.")

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Task '{task}' removed from your to-do list.")
        else:
            print(f"Task '{task}' not found.")

    def view_tasks(self):
        if self.tasks:
            print("Your to-do list::::::::::`")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("Your to-do list is empty.")

def main():
    todo_list = TodoList()
    
    while True:
        print("\n--- Todo List Menu ---")
        print("1. Add a Task")
        print("2. Remove a Task")
        print("3. View Tasks")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter the task to add: ")
            todo_list.add_task(task)
        elif choice == '2':
            task = input("Enter the task to remove: ")
            todo_list.remove_task(task)
        elif choice == '3':
            todo_list.view_tasks()
        elif choice == '4':
            print("Exiting the to-do list.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
