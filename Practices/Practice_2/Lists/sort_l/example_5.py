students = [("Alice", 25), ("Bob", 20), ("Charlie", 23)]
students.sort(key=lambda x: x[1])  # екінші элемент бойынша (жас)
print(students)  # [('Bob', 20), ('Charlie', 23), ('Alice', 25)]
