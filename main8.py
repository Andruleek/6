# Викликаємо завдання 8
def find_average_grade_given_by_teacher(teacher_name):
    cursor.execute('''SELECT AVG(grades.grade) AS average_grade, subjects.name
                      FROM grades
                      JOIN subjects ON grades.subject_id = subjects.id
                      JOIN teachers ON subjects.teacher_id = teachers.id
                      WHERE teachers.name = ?
                      GROUP BY subjects.name''', (teacher_name,))
    average_grades = cursor.fetchall()
    if average_grades:
        print(f"Average grades given by {teacher_name} in each subject:")
        for row in average_grades:
            print(f"Subject: {row[1]}, Average Grade: {row[0]}")
    else:
        print(f"No data found for {teacher_name}")

find_courses_taught_by_teacher('Jennifer Casey')

# Закриваємо підключення до бази даних
conn.close()
