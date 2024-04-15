import sqlite3
from faker import Faker
import random


# Ініціалізуємо Faker для генерації випадкових даних
fake = Faker()

# Підключаємося до бази даних
conn = sqlite3.connect('university.db')
cursor = conn.cursor()

# Створюємо таблиці
cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    group_id INTEGER)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS groups (
                    id INTEGER PRIMARY KEY,
                    name TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS teachers (
                    id INTEGER PRIMARY KEY,
                    name TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS subjects (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    teacher_id INTEGER)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS grades (
                    id INTEGER PRIMARY KEY,
                    student_id INTEGER,
                    subject_id INTEGER,
                    grade INTEGER,
                    date_received DATE)''')

# Генеруємо дані для студентів, груп, викладачів та предметів
def generate_data():
    groups = ['Group A', 'Group B', 'Group C']
    for group_name in groups:
        cursor.execute('''INSERT INTO groups (name) VALUES (?)''', (group_name,))

    for _ in range(30):
        student_name = fake.name()
        group_id = random.randint(1, len(groups))
        cursor.execute('''INSERT INTO students (name, group_id) VALUES (?, ?)''', (student_name, group_id))

    # Створення списку з трьох випадкових імен учителів
    teachers = [fake.name() for _ in range(3)]

    # Цикл для вставки кожного імені вчителя у таблицю
    for teacher_name in teachers:
        cursor.execute('''INSERT INTO teachers (name) VALUES (?)''', (teacher_name,))
    
    subjects = [('Mathematics', 1), ('Physics', 2), ('Biology', 3), ('Chemistry', 1), ('History', 2)]
    for subject in subjects:
        cursor.execute('''INSERT INTO subjects (name, teacher_id) VALUES (?, ?)''', subject)

    # Генеруємо випадкові оцінки для студентів
    for student_id in range(1, 31):
        for subject_id in range(1, 6):
            grade = random.randint(60, 100)
            date_received = fake.date_between(start_date='-3y', end_date='today')
            cursor.execute('''INSERT INTO grades (student_id, subject_id, grade, date_received) 
                              VALUES (?, ?, ?, ?)''', (student_id, subject_id, grade, date_received))

    # Зберігаємо зміни
    conn.commit()

# Запускаємо функцію для генерації даних
generate_data()

# Викликаємо завдання 10
def find_courses_taught_to_student_by_teacher(student_name, teacher_name):
    cursor.execute('''SELECT subjects.name
                      FROM subjects
                      JOIN grades ON subjects.id = grades.subject_id
                      JOIN students ON grades.student_id = students.id
                      JOIN teachers ON subjects.teacher_id = teachers.id
                      WHERE students.name = ? AND teachers.name = ?''', (student_name, teacher_name))
    courses_taught = cursor.fetchall()
    if courses_taught:
        print(f"Courses taught by {teacher_name} to {student_name}:")
        for course in courses_taught:
            print(course[0])
    else:
        print(f"No courses found for {student_name} taught by {teacher_name}")

# Викликаємо функцію для знаходження курсів, які відвідує певний студент, викладачем якого є певна особа
find_courses_taught_to_student_by_teacher('Donna Williamson', 'Jennifer Casey')

# Закриваємо підключення до бази даних
conn.close()
