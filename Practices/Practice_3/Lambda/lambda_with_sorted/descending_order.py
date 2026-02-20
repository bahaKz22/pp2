numbers = [5, 2, 9, 1, 7]

# Sort numbers descending with lambda
sorted_numbers = sorted(numbers, key=lambda x: -x)

print(sorted_numbers)  # Output: [9, 7, 5, 2, 1]