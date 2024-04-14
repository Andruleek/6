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

# Завдання 2: Знаходження найкращого студента з певного предмета
def find_top_student_in_subject(subject_name):
    cursor.execute('''SELECT students.id, students.name, AVG(grades.grade) AS avg_grade
                      FROM students
                      JOIN grades ON students.id = grades.student_id
                      JOIN subjects ON grades.subject_id = subjects.id
                      WHERE subjects.name = ?
                      GROUP BY students.id, students.name
                      ORDER BY avg_grade DESC
                      LIMIT 1''', (subject_name,))
    top_student = cursor.fetchone()
    if top_student:
        print(f"Top student in {subject_name}:")
        print(f"Student ID: {top_student[0]}, Name: {top_student[1]}, Average Grade: {top_student[2]}")
    else:
        print(f"No data found for {subject_name}")

# Викликаємо функцію для завдання 2
find_top_student_in_subject('Mathematics')

# Завдання 3: Знаходження середнього балу по групах для певного предмета
def find_average_grade_by_group(subject_name):
    cursor.execute('''SELECT groups.name, AVG(grades.grade) AS avg_grade
                      FROM groups
                      JOIN students ON groups.id = students.group_id
                      JOIN grades ON students.id = grades.student_id
                      JOIN subjects ON grades.subject_id = subjects.id
                      WHERE subjects.name = ?
                      GROUP BY groups.id, groups.name''', (subject_name,))
    average_grades = cursor.fetchall()
    if average_grades:
        print(f"Average grades in {subject_name} by group:")
        for group in average_grades:
            print(f"Group: {group[0]}, Average Grade: {group[1]}")
    else:
        print(f"No data found for {subject_name}")

# Викликаємо функцію для завдання 3
find_average_grade_by_group('Mathematics')

# Завдання 4: Знаходження середнього балу загалом
def find_average_grade_overall():
    cursor.execute('''SELECT AVG(grade) AS avg_grade_overall FROM grades''')
    average_grade_overall = cursor.fetchone()[0]
    print(f"Average grade overall: {average_grade_overall}")

# Викликаємо функцію для завдання 4
find_average_grade_overall()

# Викликаємо завдання 5
def find_courses_taught_by_teacher(teacher_name):
    cursor.execute('''SELECT subjects.name
                      FROM subjects
                      JOIN teachers ON subjects.teacher_id = teachers.id
                      WHERE teachers.name = ?''', (teacher_name,))
    courses_taught = cursor.fetchall()
    if courses_taught:
        print(f"Courses taught by {teacher_name}:")
        for course in courses_taught:
            print(course[0])
    else:
        print(f"No courses found for {teacher_name}")

# Викликаємо функцію для знаходження курсів, які читає певний викладач
find_courses_taught_by_teacher('Kathleen Sawyer')


# Викликаємо завдання 6
def find_students_in_group(group_name):
    cursor.execute('''SELECT students.name
                      FROM students
                      JOIN groups ON students.group_id = groups.id
                      WHERE groups.name = ?''', (group_name,))
    students_in_group = cursor.fetchall()
    if students_in_group:
        print(f"Students in group {group_name}:")
        for student in students_in_group:
            print(student[0])
    else:
        print(f"No students found in group {group_name}")

# Викликаємо функцію для знаходження студентів у певній групі
find_students_in_group('Group C')


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


# Викликаємо завдання 8
def find_average_grade_given_by_teacher(teacher_name):
    cursor.execute('''SELECT AVG(grades.grade) AS average_grade, subjects.name
                      FROM grades
                      JOIN subjects ON grades.subject_id = subjects.id
                      JOIN teachers ON subjects.teacher_id = teachers.id
                      WHERE teachers.name = ?
                      GROUP BY subjects.name''', (teacher_name,))
    average_grades = cursor.fetchall()
    if average_grades:
        print(f"Average grades given by {teacher_name} in each subject:")
        for row in average_grades:
            print(f"Subject: {row[1]}, Average Grade: {row[0]}")
    else:
        print(f"No data found for {teacher_name}")

find_courses_taught_by_teacher('Jennifer Casey')
 
# Моє завдання
def display_all_teachers():
    cursor.execute('''SELECT name FROM teachers''')
    all_teachers = cursor.fetchall()
    if all_teachers:
        print("All teachers:")
        for teacher in all_teachers:
            print(teacher[0])
    else:
        print("No teachers found")

# Виклик функції для виведення всіх імен вчителів
display_all_teachers()


# Викликаємо завдання 9
def find_courses_attended_by_student(student_name):
    cursor.execute('''SELECT subjects.name
                      FROM subjects
                      JOIN grades ON subjects.id = grades.subject_id
                      JOIN students ON grades.student_id = students.id
                      WHERE students.name = ?''', (student_name,))
    courses_attended = cursor.fetchall()
    if courses_attended:
        print(f"Courses attended by {student_name}:")
        for course in courses_attended:
            print(course[0])
    else:
        print(f"No courses found for {student_name}")

# Викликаємо функцію для знаходження курсів, які відвідує певний студент
find_courses_attended_by_student('Donna Williamson')

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
