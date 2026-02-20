class Person:
    species = "Human"  # Class variable

    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age    # Instance variable

# Create objects
p1 = Person("Ali", 25)
p2 = Person("Sara", 20)

# Access class variable
print(p1.species)  # Output: Human
print(p2.species)  # Output: Human


p1.species = "Alien"  # Creates an instance variable only for p1

print(p1.species)  # Output: Alien
print(p2.species)  # Output: Homo sapiens