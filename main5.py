# Викликаємо завдання 5
def find_courses_taught_by_teacher(teacher_name):
    cursor.execute('''SELECT subjects.name
                      FROM subjects
                      JOIN teachers ON subjects.teacher_id = teachers.id
                      WHERE teachers.name = ?''', (teacher_name,))
    courses_taught = cursor.fetchall()
    if courses_taught:
        print(f"Courses taught by {teacher_name}:")
        for course in courses_taught:
            print(course[0])
    else:
        print(f"No courses found for {teacher_name}")

# Викликаємо функцію для знаходження курсів, які читає певний викладач
find_courses_taught_by_teacher('Kathleen Sawyer')

# Закриваємо підключення до бази даних
conn.close()
