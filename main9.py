# Викликаємо завдання 9
def find_courses_attended_by_student(student_name):
    cursor.execute('''SELECT subjects.name
                      FROM subjects
                      JOIN grades ON subjects.id = grades.subject_id
                      JOIN students ON grades.student_id = students.id
                      WHERE students.name = ?''', (student_name,))
    courses_attended = cursor.fetchall()
    if courses_attended:
        print(f"Courses attended by {student_name}:")
        for course in courses_attended:
            print(course[0])
    else:
        print(f"No courses found for {student_name}")

# Викликаємо функцію для знаходження курсів, які відвідує певний студент
find_courses_attended_by_student('Donna Williamson')

# Закриваємо підключення до бази даних
conn.close()
