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

# Викликаємо завдання 7
def find_out_the_grades_of_students_from_the_same_group_in_the_singing_subject(subject_name, group_name):
    cursor.execute('''SELECT students.name, grades.grade
                      FROM students
                      JOIN groups ON students.group_id = groups.id
                      JOIN grades ON students.id = grades.student_id
                      JOIN subjects ON grades.subject_id = subjects.id
                      WHERE groups.name = ? AND subjects.name = ?''', (group_name, subject_name))
    student_grades = cursor.fetchall()
    if student_grades:
        print(f"Grades of students in group {group_name} for {subject_name}:")
        for student_grade in student_grades:
            print(f"Student: {student_grade[0]}, Grade: {student_grade[1]}")
    else:
        print(f"No grades found for students in group {group_name} for {subject_name}")

# Виклик функції для знаходження оцінок студентів у групі 'Group B' з предмету 'History'
find_out_the_grades_of_students_from_the_same_group_in_the_singing_subject('History', 'Group B')

# Закриваємо підключення до бази даних
conn.close()
