# Parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is", self.name)

# Child class
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # Call parent constructor
        self.student_id = student_id

    def show_id(self):
        print("My student ID is", self.student_id)

# Create object of child class
s1 = Student("Ali", 20, "S123")

s1.greet()      # From parent class
s1.show_id()    # From child class