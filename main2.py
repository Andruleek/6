from faker import Faker
import random

# Ініціалізуємо генератор Faker
fake = Faker()

# Генеруємо фіктивну базу даних студентів та їхніх оцінок
students = []
for _ in range(50):  # Генеруємо 50 студентів
    student = {
        'name': fake.name(),
        'math_grade': random.randint(60, 100),  # Оцінка з математики
    }
    students.append(student)

# Функція для знаходження студента з найвищим середнім балом з певного предмета
def find_top_student(subject, student_list):
    top_student = max(student_list, key=lambda x: x[subject+'_grade'])
    return top_student

# Знаходимо студента з найвищим середнім балом з математики
top_math_student = find_top_student('math', students)

# Виводимо інформацію про студента з найвищим балом з математики
print("Студент з найвищим балом з математики:")
print("Ім'я:", top_math_student['name'])
print("Бал з математики:", top_math_student['math_grade'])


def function_from_main2():
    print("This is a function from main.py")

