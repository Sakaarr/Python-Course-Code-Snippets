#TO DO LIST USING PYTHON CLI(COMMAND LINE INTERFACE)

FILE = "to_do_list.txt"

def load_tasks():
    try:
        with open(FILE, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []
    
def save_tasks(tasks):
    with open(FILE, 'w') as file:
        for task in tasks:
            file.write(task + '\n')
to_do_list = load_tasks()

while True:
    print("\nTo-Do List CLI")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        task = input("Enter the task: ")
        to_do_list.append(task)
        save_tasks(to_do_list)
        print(f"Task '{task}' added.")
    elif choice == '2':
        if not to_do_list:
            print("No tasks in the list.")
        else:
            print("To-Do List:")
            for i, task in enumerate(to_do_list, start=1):
                print(f"{i}. {task}")
    elif choice == '3':
        if not to_do_list:
            print("No tasks to remove.")
        else:
            for i,task in enumerate(to_do_list, start=1):
                print(f"{i}. {task}")
            try:
                task_num = int(input("Enter the task number to remove: "))
                removed = to_do_list.pop(task_num - 1)
                print(f"Task '{removed}' removed.")
            except:
                print("Invalid task number.")
    elif choice == '4':
        print("Exiting the To-Do List CLI.")
        break
    
    else:
        print("Invalid choice. Please try again.")