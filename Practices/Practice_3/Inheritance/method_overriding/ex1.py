# Parent class
class Person:
    def greet(self):
        print("Hello from Person")

# Child class
class Student(Person):
    def greet(self):
        print("Hello from Student")  # Overrides parent method

# Create objects
p1 = Person()
s1 = Student()

p1.greet()  # Output: Hello from Person
s1.greet()  # Output: Hello from Student