from abc import ABC, abstractmethod

# 🔹 Abstract Class (Abstraction)
class Person(ABC):
    def __init__(self, name, age):
        self._name = name          # Encapsulation (_protected)
        self._age = age

    @abstractmethod
    def display_info(self):
        pass

# 🔹 Student Class (Inheritance from Person)
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.__student_id = student_id  # Private attribute

    def display_info(self):
        print(f"Student Name: {self._name}")
        print(f"Age: {self._age}")
        print(f"Student ID: {self.__student_id}")

# 🔹 Teacher Class (Inheritance from Person)
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display_info(self):
        print(f"Teacher Name: {self._name}")
        print(f"Age: {self._age}")
        print(f"Subject: {self.subject}")

# 🔹 Polymorphism Function
def show_person_details(person: Person):
    person.display_info()
    print("-" * 30)

# 🔹 Management System Class
class ManagementSystem:
    def __init__(self):
        self.students = []
        self.teachers = []

    def add_student(self, name, age, student_id):
        student = Student(name, age, student_id)
        self.students.append(student)
        print("✅ Student added successfully.")

    def add_teacher(self, name, age, subject):
        teacher = Teacher(name, age, subject)
        self.teachers.append(teacher)
        print("✅ Teacher added successfully.")

    def show_all_students(self):
        print("\n📚 All Students:")
        for student in self.students:
            show_person_details(student)

    def show_all_teachers(self):
        print("\n👨‍🏫 All Teachers:")
        for teacher in self.teachers:
            show_person_details(teacher)

# 🔹 Main Menu Loop
def main():
    system = ManagementSystem()

    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. Add Teacher")
        print("3. Show All Students")
        print("4. Show All Teachers")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter Student Name: ")
            age = int(input("Enter Age: "))
            sid = input("Enter Student ID: ")
            system.add_student(name, age, sid)

        elif choice == '2':
            name = input("Enter Teacher Name: ")
            age = int(input("Enter Age: "))
            subject = input("Enter Subject: ")
            system.add_teacher(name, age, subject)

        elif choice == '3':
            system.show_all_students()

        elif choice == '4':
            system.show_all_teachers()

        elif choice == '5':
            print("👋 Exiting Program. Bye!")
            break

        else:
            print("❌ Invalid choice. Please try again.")

# 🔹 Run the main function
if __name__ == "__main__":
    main()
