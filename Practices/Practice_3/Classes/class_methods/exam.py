class Person:
    species = "Human"  # Class attribute

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def show_species(cls):
        print("Species:", cls.species)

# Call class method using the class
Person.show_species()  # Output: Species: Human