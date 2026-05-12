
sum_students = int(input())
grade_students = 0
total_grade = 0
students_top = 0
students_4 = 0
students_3 = 0
students_fail = 0


for _ in range(sum_students):
    grade_students = float(input())
    total_grade += grade_students

    if grade_students >= 5:
        students_top += 1
    elif 4 <= grade_students <= 4.99:
        students_4 += 1
    elif 3 <= grade_students <= 3.99:
        students_3 += 1
    elif grade_students < 3:
        students_fail += 1

perc_top = students_top / sum_students * 100
perc_4 = students_4 / sum_students * 100
perc_3 = students_3 / sum_students * 100
perc_fail = students_fail / sum_students * 100

average_score = total_grade / sum_students

print(f"Top students: {perc_top:.2f}%")
print(f"Between 4.00 and 4.99: {perc_4:.2f}%")
print(f"Between 3.00 and 3.99: {perc_3:.2f}%")
print(f"Fail: {perc_fail:.2f}%")
print(f"Average: {average_score:.2f}")