from faker import Faker
import pandas as pd
import random

# Ініціалізуємо Faker для генерації випадкових даних
fake = Faker()

# Задаємо кількість викладачів та предметів
num_teachers = 10
num_subjects_per_teacher = 3

# Генеруємо дані для викладачів та предметів
data = []
for _ in range(num_teachers):
    teacher_name = fake.name()
    for _ in range(num_subjects_per_teacher):
        subject_name = fake.word()
        # Генеруємо випадкові оцінки від 1 до 10 для кожного предмету
        grades = [random.randint(1, 10) for _ in range(10)]
        data.append([teacher_name, subject_name] + grades)

# Створюємо DataFrame зі згенерованими даними
columns = ['Teacher', 'Subject'] + [f'Grade_{i+1}' for i in range(10)]
df = pd.DataFrame(data, columns=columns)

# Функція для знаходження середнього балу викладача з предмету
def average_grade_for_teacher_subject(teacher_name, subject_name):
    teacher_subject_df = df[(df['Teacher'] == teacher_name) & (df['Subject'] == subject_name)]
    if len(teacher_subject_df) == 0:
        return None
    grades = teacher_subject_df.iloc[:, 2:].values.flatten()
    return sum(grades) / len(grades)

# Приклад використання функції для знаходження середнього балу певного викладача з предмету
teacher_name = df['Teacher'].iloc[0]
subject_name = df['Subject'].iloc[0]
average_grade = average_grade_for_teacher_subject(teacher_name, subject_name)
print(f"Середній бал викладача {teacher_name} з предмету {subject_name}: {average_grade}")


def function_from_main8():
    print("This is a function from main8.py")