# SIMPLE TO-DO LIST APP
# Add, view, and remove tasks.

todo_list = []

while True:
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        task = input("Enter task: ")
        todo_list.append(task)
        print("✅ Task added!")
    elif choice == '2':
        print("\nYour Tasks:")
        if not todo_list:
            print("No tasks yet!")
        else:
            for i, task in enumerate(todo_list, start=1):
                print(f"{i}. {task}")
    elif choice == '3':
        task_no = int(input("Enter task number to remove: "))
        if 0 < task_no <= len(todo_list):
            removed = todo_list.pop(task_no - 1)
            print(f"❌ Task '{removed}' removed.")
        else:
            print("Invalid task number!")
    elif choice == '4':
        print("Goodbye! 👋")
        break
    else:
        print("Invalid input. Please choose 1-4.")