from faker import Faker
import random

fake = Faker('uk_UA')

# Створення списку курсів
courses = [fake.job() for _ in range(10)]

# Створення списку студентів та викладачів
students = [fake.name() for _ in range(20)]
teachers = [fake.name() for _ in range(5)]

# Створення словника, що зв'язує кожного студента з його курсами
students_courses = {student: random.sample(courses, random.randint(1, 3)) for student in students}

# Створення словника, що зв'язує кожен курс з викладачем
courses_teachers = {course: random.choice(teachers) for course in courses}

# Функція для знаходження курсів, які відвідує певний студент
def find_courses_for_student(student_name):
    if student_name in students_courses:
        return students_courses[student_name]
    else:
        return "Студент не знайдений"

# Функція для знаходження викладача, який веде певний курс
def find_teacher_for_course(course_name):
    if course_name in courses_teachers:
        return courses_teachers[course_name]
    else:
        return "Курс не знайдений"

# Приклад використання
student_name = random.choice(students)
print(f"Студент {student_name} відвідує курси:")
print(find_courses_for_student(student_name))

course_name = random.choice(courses)
print(f"Курс {course_name} веде викладач:")
print(find_teacher_for_course(course_name))


def function_from_main10():
    print("This is a function from main10.py")