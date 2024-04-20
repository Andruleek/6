import sqlite3
from faker import Faker
import random


# Ініціалізуємо Faker для генерації випадкових даних
fake = Faker()

# Підключаємося до бази даних
conn = sqlite3.connect('university.db')
cursor = conn.cursor()

# Завдання 4: Знаходження середнього балу загалом
def find_average_grade_overall():
    cursor.execute('''SELECT AVG(grade) AS avg_grade_overall FROM grades''')
    average_grade_overall = cursor.fetchone()[0]
    print(f"Average grade overall: {average_grade_overall}")

# Викликаємо функцію для завдання 4
find_average_grade_overall()

# Закриваємо підключення до бази даних
conn.close()
