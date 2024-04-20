import sqlite3
from faker import Faker
import random


# Ініціалізуємо Faker для генерації випадкових даних
fake = Faker()

# Підключаємося до бази даних
conn = sqlite3.connect('university.db')
cursor = conn.cursor()

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
