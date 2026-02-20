class Person:
    species = "Human"

    @classmethod
    def change_species(cls, new_species):
        cls.species = new_species

# Change the class attribute
Person.change_species("Homo sapiens")
print(Person.species)  # Output: Homo sapiens