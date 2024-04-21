import sqlite3
from faker import Faker
import random
from main2 import function_from_main2
from main3 import function_from_main3
from main4 import function_from_main4
from main5 import function_from_main5
from main6 import function_from_main6
from main7 import function_from_main7
from main8 import function_from_main8
from main9 import function_from_main9
from main10 import function_from_main10

# Виклик функцій з імпортованих файлів
function_from_main2()
function_from_main3()
function_from_main4()
function_from_main5()
function_from_main6()
function_from_main7()
function_from_main8()
function_from_main9()
function_from_main10()

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
    groups = ['Group 1', 'Group 2', 'Group 3']
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
        
    subjects = [('Mathematics', 1), ('Physics', 2), ('Biology', 3), ('Chemistry', 4), ('History', 5)]
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

# Завдання 1: Знаходження 5 студентів з найбільшим середнім балом
def find_top_students():
    cursor.execute('''SELECT students.id, students.name, AVG(grades.grade) AS avg_grade
                      FROM students
                      JOIN grades ON students.id = grades.student_id
                      GROUP BY students.id, students.name
                      ORDER BY avg_grade DESC
                      LIMIT 5''')

    top_students = cursor.fetchall()

    print("Top 5 students with highest average grades:")
    for student in top_students:
        print(f"Student ID: {student[0]}, Name: {student[1]}, Average Grade: {student[2]}")

# Викликаємо функцію для завдання 1
find_top_students()


# Закриваємо підключення до бази даних
conn.close()
