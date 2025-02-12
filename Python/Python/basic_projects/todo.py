tasks = []

while True:
    print("\n1. Add Task\n2. View Tasks\n3. Remove Task\n4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        print("\nTo-Do List:")
        if not tasks:
            print("No tasks available.")
        else:
            for idx, task in enumerate(tasks, 1):
                print(f"{idx}. {task}")

    elif choice == "3":
        if not tasks:
            print("No tasks to remove.")
        else:
            try:
                task_num = int(input("Enter task number to remove: "))
                if 0 < task_num <= len(tasks):
                    tasks.pop(task_num - 1)
                    print("Task removed!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Try again.")
