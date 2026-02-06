grades = {"Alice": 85, "Bob": 90}
new_students = {"Charlie": 78, "David": 92}
for student, score in new_students.items():
    grades[student] = score
print(grades)  # {'Alice': 85, 'Bob': 90, 'Charlie': 78, 'David': 92}
