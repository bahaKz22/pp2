students = {
    "student1": {"name": "Alice", "age": 25},
    "student2": {"name": "Bob", "age": 30}
}

for student_id, info in students.items():
    print(student_id)
    for key, value in info.items():
        print(f"  {key}: {value}")
