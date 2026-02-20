numbers = [1, 2, 3, 4, 5, 6]

# Use filter with lambda to keep only even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)  # Output: [2, 4, 6]