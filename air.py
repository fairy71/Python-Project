import sqlite3

def connect_db():
    return sqlite3.connect("students.db")

def create_tables():
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        major TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS courses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        course_name TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS grades (
        student_id INTEGER,
        course_id INTEGER,
        score REAL,
        FOREIGN KEY(student_id) REFERENCES students(id),
        FOREIGN KEY(course_id) REFERENCES courses(id)
    )
    """)

    conn.commit()
    conn.close()


from database import connect_db

def add_student(name, age, major):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO students (name, age, major) VALUES (?, ?, ?)",
                (name, age, major))
    conn.commit()
    conn.close()

def show_students():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    for row in cur.fetchall():
        print(row)
    conn.close()

from database import connect_db

def add_course(course_name):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO courses (course_name) VALUES (?)",
                (course_name,))
    conn.commit()
    conn.close()


from database import connect_db

def add_grade(student_id, course_id, score):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO grades (student_id, course_id, score) VALUES (?, ?, ?)",
        (student_id, course_id, score)
    )
    conn.commit()
    conn.close()

def show_grades():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
    SELECT s.name, c.course_name, g.score
    FROM grades g
    JOIN students s ON g.student_id = s.id
    JOIN courses c ON g.course_id = c.id
    """)
    for row in cur.fetchall():
        print(row)
    conn.close()


from database import create_tables
from student import add_student, show_students
from course import add_course
from grade import add_grade, show_grades

create_tables()

while True:
    print("\n1. Thêm sinh viên")
    print("2. Thêm môn học")
    print("3. Nhập điểm")
    print("4. Xem danh sách sinh viên")
    print("5. Xem bảng điểm")
    print("0. Thoát")

    choice = input("Chọn: ")

    if choice == "1":
        name = input("Tên: ")
        age = int(input("Tuổi: "))
        major = input("Ngành: ")
        add_student(name, age, major)

    elif choice == "2":
        course = input("Tên môn: ")
        add_course(course)

    elif choice == "3":
        sid = int(input("ID sinh viên: "))
        cid = int(input("ID môn: "))
        score = float(input("Điểm: "))
        add_grade(sid, cid, score)

    elif choice == "4":
        show_students()

    elif choice == "5":
        show_grades()

    elif choice == "0":
        break


