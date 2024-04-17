# Викликаємо завдання 6
def find_students_in_group(group_name):
    cursor.execute('''SELECT students.name
                      FROM students
                      JOIN groups ON students.group_id = groups.id
                      WHERE groups.name = ?''', (group_name,))
    students_in_group = cursor.fetchall()
    if students_in_group:
        print(f"Students in group {group_name}:")
        for student in students_in_group:
            print(student[0])
    else:
        print(f"No students found in group {group_name}")

# Викликаємо функцію для знаходження студентів у певній групі
find_students_in_group('Group C')

# Закриваємо підключення до бази даних
conn.close()
