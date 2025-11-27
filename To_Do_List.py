def main():
    while True:
        print("\n---- To Do List App ----")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Edit Task")
        print("4. Complete Task")
        print("5. Delete All Tasks")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            edit_task()
        elif choice == "4":
            complete_task()
        elif choice == "5":
            delete_all_tasks()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, Try again.")

def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            tasks = [task.strip() for task in f.readlines()]
        return tasks
    except FileNotFoundError():
        return []

def save_tasks(tasks):
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")

def add_task():
    task = input("Enter new task: ")
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks available.")
    else:
        print("\n-- Your To Do List --")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def edit_task():
    tasks = load_tasks()
    if not tasks:
        print("No tasks to edit.")
        return
    
    view_tasks()

    choice = input("Enter task number to edit: ").strip()
    if not choice.isdigit():
        print("Please enter a valid number.")
        return
    
    num = int(choice)
    if 1 <= num <= len(tasks):
        current = tasks[num - 1]
        print(f"Current task #{num}: {current}")
        new_text = input("Enter new text for this task: ").strip()
        if not new_text:
            print("Empty input - Task not changed.")
            return
        tasks[num - 1] = new_text
        save_tasks(tasks)
        print(f"Task #{num} updated successfuly!")
    else:
        print("Invalid task number.")

def complete_task():
    tasks = load_tasks()
    view_tasks()
    if tasks:
        num = int(input("Enter task number to mark as completed: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"Task '{removed}' marked as completed!")
        else:
            print("Inavalid task number.")

def delete_all_tasks():
    open("tasks.txt", "w").close()
    print("All tasks deleted!")

if __name__ == "__main__":
    main()