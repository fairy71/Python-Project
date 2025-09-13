# Quiz Game

questions = {
    "What is the capital of France?": ["a. Paris", "b. London", "c. Rome", "a"],
    "Which language is used for AI?": ["a. Python", "b. C++", "c. Java", "a"],
    "2 + 2 = ?": ["a. 3", "b. 4", "c. 5", "b"]
}

score = 0

for q, opts in questions.items():
    print("\n" + q)
    for option in opts[:-1]:
        print(option)
    ans = input("Your answer (a/b/c): ").lower()
    if ans == opts[-1]:
        print(" Correct!")
        score += 1
    else:
        print(" Wrong! Correct answer:", opts[-1])

print(f"\nYour Final Score: {score}/{len(questions)}")














import tkinter as tk
import time

def update_time():
    current_time = time.strftime("%H:%M:%S")
    label.config(text=current_time)
    root.after(1000, update_time)  

root = tk.Tk()
root.title("Digital Clock")

label = tk.Label(root, font=("Arial", 50), fg="blue")
label.pack()

update_time()
root.mainloop()





# Digital Clock using Tkinter
import tkinter as tk
import time

def update_time():
    current_time = time.strftime("%H:%M:%S")
    label.config(text=current_time)
    root.after(1000, update_time)  

root = tk.Tk()
root.title("Digital Clock")

label = tk.Label(root, font=("Arial", 50), fg="blue")
label.pack()

update_time()
root.mainloop()





# Contact Book

contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    contacts[name] = phone
    print(Contact added successfully!")

def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        print(f" {name}: {contacts[name]}")
    else:
        print(" Contact not found!")

def display_contacts():
    if not contacts:
        print("No contacts available.")
    else:
        print("\n--- Contact List ---")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")

while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Display All Contacts")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        display_contacts()
    elif choice == "4":
        print("Goodbye ")
        break
    else:
        print("Invalid choice! Try again.")