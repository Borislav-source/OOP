import statistics

rows_count = int(input())
students = {}

for _ in range(rows_count):
    student_name = input()
    grade = float(input())
    if student_name not in students:
        students[student_name] = []
    students[student_name].append(grade)

for student in students:
    students[student] = statistics.mean(students[student])


for student in dict(sorted(students.items(), key=lambda x: x[1], reverse=True)):
    if students[student] >= 4.5:
        print(f'{student} -> {students[student]:.2f}')


