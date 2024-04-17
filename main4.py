# Завдання 4: Знаходження середнього балу загалом
def find_average_grade_overall():
    cursor.execute('''SELECT AVG(grade) AS avg_grade_overall FROM grades''')
    average_grade_overall = cursor.fetchone()[0]
    print(f"Average grade overall: {average_grade_overall}")

# Викликаємо функцію для завдання 4
find_average_grade_overall()

# Закриваємо підключення до бази даних
conn.close()
