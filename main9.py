from faker import Faker
import random

fake = Faker()

# Генеруємо випадкових студентів
def generate_students(num_students):
    students = []
    for _ in range(num_students):
        student = {
            "id": fake.uuid4(),
            "name": fake.name(),
            "courses": generate_courses(random.randint(1, 5))  # Генеруємо випадкову кількість курсів для кожного студента
        }
        students.append(student)
    return students

# Генеруємо випадкові курси
def generate_courses(num_courses):
    courses = []
    for _ in range(num_courses):
        course = {
            "id": fake.uuid4(),
            "name": fake.job(),
            "teacher": fake.name(),
            "time": fake.time()
        }
        courses.append(course)
    return courses

# Функція для пошуку курсів, які відвідує студент
def find_student_courses(students, student_name):
    for student in students:
        if student["name"] == student_name:
            return student["courses"]
    return None

# Генеруємо випадкових студентів та курси
students = generate_students(5)
print("Список студентів та їх курсів:")
for student in students:
    print("Студент:", student["name"])
    print("Курси:")
    for course in student["courses"]:
        print("- ", course["name"])
    print()

# Приклад пошуку курсів для певного студента
student_name = input("Введіть ім'я студента для пошуку його курсів: ")
student_courses = find_student_courses(students, student_name)
if student_courses:
    print(f"Курси, які відвідує студент {student_name}:")
    for course in student_courses:
        print("- ", course["name"])
else:
    print("Студент не знайдений.")

def function_from_main9():
    print("This is a function from main9.py")