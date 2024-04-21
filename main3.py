from faker import Faker
import random

# Ініціалізація Faker для генерації випадкових даних
fake = Faker()

# Створення бази даних студентів та їх оцінок
students = []
for _ in range(50):  # Припустимо, що ми маємо 100 студентів
    student = {
        "name": fake.name(),
        "subject": fake.random_element(elements=("Biology", "Physics", "Chemistry")),
        "grade": random.randint(1, 100)  # Випадкові оцінки від 1 до 10
    }
    students.append(student)

# Функція для знаходження середнього балу у групах з певного предмету
def average_grade_by_subject(students, subject):
    grades = [student["grade"] for student in students if student["subject"] == subject]
    if grades:
        return sum(grades) / len(grades)
    else:
        return 0  # Повертаємо 0, якщо не знайдено жодної оцінки для вказаного предмету

# Приклад використання функції для знаходження середнього балу з математики
math_average = average_grade_by_subject(students, "Biology")
print("Середній бал з математики:", math_average)

# Приклад використання функції для знаходження середнього балу з фізики
physics_average = average_grade_by_subject(students, "Physics")
print("Середній бал з фізики:", physics_average)

# Приклад використання функції для знаходження середнього балу з хімії
chemistry_average = average_grade_by_subject(students, "Chemistry")
print("Середній бал з хімії:", chemistry_average)

def function_from_main3():
    print("This is a function from main3.py")
