from faker import Faker
import random

fake = Faker()

# Створимо випадкову базу даних оцінок
num_students = 1000
num_subjects = 5
num_scores_per_student = 4

scores = []
for student_id in range(1, num_students + 1):
    for subject_id in range(1, num_subjects + 1):
        for _ in range(num_scores_per_student):
            scores.append({
                'student_id': student_id,
                'subject_id': subject_id,
                'score': random.randint(60, 100)  # випадкові оцінки від 60 до 100
            })

# Знайдемо середній бал на потоці
total_score = 0
total_count = 0

for score in scores:
    total_score += score['score']
    total_count += 1

average_score = total_score / total_count

print("Середній бал на потоці: {:.2f}".format(average_score))
 
def function_from_main4():
    print("This is a function from main4.py")
