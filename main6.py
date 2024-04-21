from faker import Faker
import random

fake = Faker()

# Генеруємо список студентів та їх груп
def generate_students(num_students, num_groups):
    students = []
    for _ in range(num_students):
        student = {
            'name': fake.name(),
            'group': random.randint(1, num_groups)
        }
        students.append(student)
    return students

# Знайти список студентів у певній групі
def find_students_in_group(students, group_number):
    return [student['name'] for student in students if student['group'] == group_number]

# Приклад використання
if __name__ == "__main__":
    num_students = 50
    num_groups = 3
    
    students = generate_students(num_students, num_groups)
    print("Список студентів у групах:")
    for group_num in range(1, num_groups + 1):
        group_students = find_students_in_group(students, group_num)
        print(f"Група {group_num}: {group_students}")

def function_from_main6():
    print("This is a function from main6.py")
