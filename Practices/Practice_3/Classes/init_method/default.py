class Person:
    def __init__(self, name="Guest", age=0):
        self.name = name
        self.age = age

p1 = Person()           # Use default values
p2 = Person("Sara", 20) # Custom values

print(p1.name, p1.age)  # Output: Guest 0
print(p2.name, p2.age)  # Output: Sara 20