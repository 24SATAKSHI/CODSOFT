import os

def print_todo_list(todo_list):
    print("Your To-Do List:")
    for index, task in enumerate(todo_list, start=1):
        print(f"{index}. {task}")
    print()

def add_task(todo_list, task):
    todo_list.append(task)
    save_todo_list(todo_list)
    print("Task added successfully!")

def remove_task(todo_list, task_index):
    if 1 <= task_index <= len(todo_list):
        removed_task = todo_list.pop(task_index - 1)
        save_todo_list(todo_list)
        print(f"Task '{removed_task}' removed successfully!")
    else:
        print("Invalid task index. No task removed.")

def save_todo_list(todo_list):
    with open("todo_list.txt", "w") as file:
        for task in todo_list:
            file.write(task + "\n")

def load_todo_list():
    if os.path.exists("todo_list.txt"):
        with open("todo_list.txt", "r") as file:
            todo_list = file.read().splitlines()
    else:
        todo_list = []
    return todo_list

def main():
    todo_list = load_todo_list()

    while True:
        print_todo_list(todo_list)

        print("Options:")
        print("1. Add task")
        print("2. Remove task")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            task = input("Enter the task: ")
            add_task(todo_list, task)
        elif choice == "2":
            task_index = int(input("Enter the task index to remove: "))
            remove_task(todo_list, task_index)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
