cars = ["BMW","KYANYSH","AUDI","TOYOTA","LEXUS","MAZDA","OPEL"]

print("Example 1: enumerate()")

for index, car in enumerate(cars):
    print(index,car)
print()

print("Example 2: enumerate(start=1)")

for index, car in enumerate(cars, start=1):
    print(index,car)
print()

print("Example 3: zip()")

name = ["Kuanish","Sungat","Bagdaulet","Bekzat"]
birthday = ['January 10th','July 21st','May 13th','February 22nd']

for names, birthdays in zip(name,birthday):
    print(f"{names}'s birthday in {birthdays}")
print()

print("Example 4: zip to list")

result = list(zip(name,birthday))
print(result)
print()

print("Example 5: Dot Product")

a = [1,2,3]
b = [4,5,6]
dot_product = sum(x*y for x, y in zip(a,b))
print("Dot product: ", dot_product)

