# Parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Child class
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # Call parent constructor
        self.student_id = student_id

# Create object
s1 = Student("Ali", 20, "S123")

print(s1.name)       # Output: Ali
print(s1.age)        # Output: 20
print(s1.student_id) # Output: S123