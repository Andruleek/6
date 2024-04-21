from faker import Faker
import random

fake = Faker()

# Генеруємо фіктивну базу даних студентів та їх оцінок
students = [{'name': fake.name(), 'group': random.randint(1, 5), 'subject': fake.word()} for _ in range(50)]
grades = [{'student_name': student['name'], 'grade': round(random.uniform(60, 100), 2)} for student in students]

# Функція для знаходження оцінок студентів у конкретній групі з певного предмета
def find_grades(group, subject):
    group_grades = [grade['grade'] for grade in grades if grade['student_name'] in [student['name'] for student in students if student['group'] == group and student['subject'] == subject]]
    return group_grades

# Приклад використання функції
group = 3
subject = "Biology"
group_grades = find_grades(group, subject)
print(f"Оцінки студентів у групі {group} з предмета {subject}: {group_grades}")


def function_from_main7():
    print("This is a function from main7.py")
