task = [ ]

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                task.append(line.strip())
    except FileNotFoundError:
        print("No existing task file found. Starting with an empty to-do list.")

def save_tasks():
    with open("tasks.txt", "w") as file:
        for item in task:
            file.write(item + "\n")



def add_task():
    new_task = input("Enter a new task: ")
    task.append(new_task)
    print("Task added successfully.")

def view_tasks():
    if not task:
        print("No tasks in the list.")
    else:
        print("To-Do List:")
        for index, item in enumerate(task, start=1):
            print(f"{index}. {item}")

def remove_task():
    view_tasks()
    if task:
        try:
            task_number = int(input("Enter the number of the task that  you want to remove: "))
            if 1 <= task_number <= len(task):
                removed_task = task.pop(task_number - 1)
                print(f"Task '{removed_task}' removed successfully.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    load_tasks()
    while True:
        try:
            print("\nTo-Do List Menu:")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Remove Task")
            print("4. Exit")
            choice = input("Enter your choice (1-4): ")
            if choice == '1':
                add_task()
                save_tasks()
            elif choice == '2':
                view_tasks()
            elif choice == '3':
                remove_task()
                save_tasks()
            elif choice == '4':
                print("Exiting the To-Do List application. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except KeyboardInterrupt:
            print("\n\nExiting the To-Do List application. Goodbye!")
            break

if __name__ == "__main__": 
    main()


