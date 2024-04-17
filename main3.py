# Завдання 3: Знаходження середнього балу по групах для певного предмета
def find_average_grade_by_group(subject_name):
    cursor.execute('''SELECT groups.name, AVG(grades.grade) AS avg_grade
                      FROM groups
                      JOIN students ON groups.id = students.group_id
                      JOIN grades ON students.id = grades.student_id
                      JOIN subjects ON grades.subject_id = subjects.id
                      WHERE subjects.name = ?
                      GROUP BY groups.id, groups.name''', (subject_name,))
    average_grades = cursor.fetchall()
    if average_grades:
        print(f"Average grades in {subject_name} by group:")
        for group in average_grades:
            print(f"Group: {group[0]}, Average Grade: {group[1]}")
    else:
        print(f"No data found for {subject_name}")

# Викликаємо функцію для завдання 3
find_average_grade_by_group('Mathematics')

# Закриваємо підключення до бази даних
conn.close()
