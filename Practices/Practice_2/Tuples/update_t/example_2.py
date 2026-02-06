numbers = (1, 2, 3)
numbers_list = list(numbers)   # tuple → list
numbers_list[1] = 20           # өзгерту
numbers = tuple(numbers_list)  # list → tuple
print(numbers)                 # (1, 20, 3)
