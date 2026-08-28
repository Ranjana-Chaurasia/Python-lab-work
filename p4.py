# Interactive Command-Line Task Scheduler with Lazy Evaluation

tasks = []

print("----------Task Scheduler----------")
while True:

    print("\n1. Add/Process Task")
    print("2. View task queue")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\n---Add Task---")

        task = input("Enter your task: ")
        ready = input("Is task ready? ") == "yes"
        high_priority = input("Is task high priority? ") == "yes"
        urgent = input("Is task urgent? ") == "yes"
        cancelled = input("Is task cancelled? ") == "yes"

        if ready and (high_priority or urgent) and not cancelled:
            tasks.append(task)
            print("Nice! The task is executable.")

        elif cancelled:
            print("Oops! The task is cancelled.")

        elif not ready:
            print("Not executable. Complete the task.")

        else:
            print("Task is in pending.")

    elif choice == "2":
        if not tasks:
            print("\nTask queue is empty.")
        else:
            print("\n---Displaying Tasks---")
            print(tasks)

    elif choice == "3":
        print("\nExiting task scheduler. Goodbye!")
        break

    else:
        print("Invalid input.")