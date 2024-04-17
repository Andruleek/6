# Завдання 2: Знаходження найкращого студента з певного предмета
def find_top_student_in_subject(subject_name):
    cursor.execute('''SELECT students.id, students.name, AVG(grades.grade) AS avg_grade
                      FROM students
                      JOIN grades ON students.id = grades.student_id
                      JOIN subjects ON grades.subject_id = subjects.id
                      WHERE subjects.name = ?
                      GROUP BY students.id, students.name
                      ORDER BY avg_grade DESC
                      LIMIT 1''', (subject_name,))
    top_student = cursor.fetchone()
    if top_student:
        print(f"Top student in {subject_name}:")
        print(f"Student ID: {top_student[0]}, Name: {top_student[1]}, Average Grade: {top_student[2]}")
    else:
        print(f"No data found for {subject_name}")

# Викликаємо функцію для завдання 2
find_top_student_in_subject('Mathematics')

# Закриваємо підключення до бази даних
conn.close()
