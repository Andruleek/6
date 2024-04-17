# Викликаємо завдання 10
def find_courses_taught_to_student_by_teacher(student_name, teacher_name):
    cursor.execute('''SELECT subjects.name
                      FROM subjects
                      JOIN grades ON subjects.id = grades.subject_id
                      JOIN students ON grades.student_id = students.id
                      JOIN teachers ON subjects.teacher_id = teachers.id
                      WHERE students.name = ? AND teachers.name = ?''', (student_name, teacher_name))
    courses_taught = cursor.fetchall()
    if courses_taught:
        print(f"Courses taught by {teacher_name} to {student_name}:")
        for course in courses_taught:
            print(course[0])
    else:
        print(f"No courses found for {student_name} taught by {teacher_name}")

# Викликаємо функцію для знаходження курсів, які відвідує певний студент, викладачем якого є певна особа
find_courses_taught_to_student_by_teacher('Donna Williamson', 'Jennifer Casey')

# Закриваємо підключення до бази даних
conn.close()
