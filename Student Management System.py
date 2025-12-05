import json
import os

DATA_FILE = "students.json"

# Load data from JSON file
def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

# Save data to JSON file
def save_data(students):
    with open(DATA_FILE, "w") as f:
        json.dump(students, f, indent=4)

# Add new student
def add_student():
    students = load_data()
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    course = input("Enter course: ")

    student = {
        "name": name,
        "roll": roll,
        "course": course
    }

    students.append(student)
    save_data(students)
    print("Student added successfully!\n")

# View all students
def view_students():
    students = load_data()
    if not students:
        print("No student records found.\n")
        return
    
    print("\n---- Student List ----")
    for s in students:
        print(f"Name: {s['name']}, Roll: {s['roll']}, Course: {s['course']}")
    print()

# Delete a student
def delete_student():
    students = load_data()
    roll = input("Enter roll number to delete: ")

    new_students = [s for s in students if s['roll'] != roll]

    if len(new_students) == len(students):
        print("Student not found!\n")
    else:
        save_data(new_students)
        print("Student deleted successfully!\n")

# Main Menu
def main():
    while True:
        print("====== Student Management System ======")
        print("1. Add Student")
        print("2. View Students")
        print("3. Delete Student")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Try again.\n")

if __name__ == "__main__":
    main()
