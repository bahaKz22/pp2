class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

car1 = Car("Toyota", "Corolla", 2020)

print(car1.brand)  # Output: Toyota
print(car1.model)  # Output: Corolla
print(car1.year)   # Output: 2020