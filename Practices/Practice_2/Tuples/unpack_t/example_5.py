def display(name, age, job):
    print(f"{name} is {age} years old and works as {job}")

person = ("Bob", 30, "Doctor")
display(*person)
# Bob is 30 years old and works as Doctor
