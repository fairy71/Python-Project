import os
import shutil

def organize_folder(folder_path):
    if not os.path.exists(folder_path):
        print("Folder path not found!")
        return

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            file_ext = filename.split('.')[-1]
            dest_folder = os.path.join(folder_path, file_ext.upper() + "_Files")

            if no
            
            
            
            t os.path.exists(dest_folder):
                os.makedirs(dest_folder)

            shutil.move(file_path, os.path.join(dest_folder, filename))

    print("Files organized successfully!")

# Example usage
folder = input("Enter full path of folder to organize: ")
organize_folder(folder)







import os

TODO_FILE = "todo.txt"

def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, 'r') as f:
        return [line.strip() for line in f.readlines()]

def save_tasks(tasks):
    with open(TODO_FILE, 'w') as f:
        for task in tasks:
            f.write(task + '\n')

def show_tasks(tasks):
    if not tasks:
        print(" No tasks yet!")
    else:
        print("\n Your To-Do List:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
    print()

def add_task(tasks):
    task = input("Enter new task: ").strip()
    if task:
        tasks.append(task)
        print(" Task added.")
    else:
        print(" Task cannot be empty!")

def remove_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to remove: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f" Removed task: {removed}")
        else:
            print(" Invalid task number!")
    except ValueError:
        print(" Please enter a number!")

def main():
    tasks = load_tasks()

    while True:
        print("====== TO-DO MENU ======")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Save and exit")
        choice = input("Choose (1-4): ").strip()

        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            save_tasks(tasks)
            print(" Tasks saved. Goodbye!")
            break
        else:
            print(" Invalid choice. Try again!")

if __name__ == "__main__":
    main()
