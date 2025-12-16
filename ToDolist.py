tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
    elif choice == "2":
        for i, task in enumerate(tasks):
            print(i + 1, task)
    elif choice == "3":
        num = int(input("Enter task number: "))
        tasks.pop(num - 1)
    elif choice == "4":
        break
