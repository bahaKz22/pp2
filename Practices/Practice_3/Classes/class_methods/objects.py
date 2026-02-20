class Person:
    species = "Human"

    @classmethod
    def show_species(cls):
        print("Species:", cls.species)

# Create object
p1 = Person()
p1.show_species()  # Output: Species: Human