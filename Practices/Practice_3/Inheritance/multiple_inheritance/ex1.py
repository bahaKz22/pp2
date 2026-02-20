# Parent class 1
class Mother:
    def skills(self):
        print("Cooking, Painting")

# Parent class 2
class Father:
    def skills(self):
        print("Driving, Programming")

# Child class inherits from both
class Child(Mother, Father):
    pass

c1 = Child()
c1.skills()  # Output: Cooking, Painting