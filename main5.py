from faker import Faker
import random

# Створення відомостей про викладачів та курси
fake = Faker()

# Створення списку викладачів і курсів
teachers = [fake.name() for _ in range(5)]
courses = [fake.catch_phrase() for _ in range(10)]

# Генерація випадкового набору курсів для кожного викладача
teacher_courses = {teacher: random.sample(courses, random.randint(1, 5)) for teacher in teachers}

# Виведення випадкових відомостей про викладачів та курси
print("Викладачі та курси:")
for teacher, teacher_course_list in teacher_courses.items():
    print(f"Викладач: {teacher}")
    print("Курси:", ", ".join(teacher_course_list))
    print()

# Пошук курсів для певного викладача
target_teacher = random.choice(teachers)
print(f"Курси, які читає викладач {target_teacher}:")
print(", ".join(teacher_courses[target_teacher]))

def function_from_main5():
    print("This is a function from main5.py")
