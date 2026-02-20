class Person:
    def greet(self):
        print("Hello from Person")

class Student(Person):
    def greet(self):
        super().greet()  # Call parent method
        print("Hello from Student")  # Add extra behavior

s1 = Student()
s1.greet()