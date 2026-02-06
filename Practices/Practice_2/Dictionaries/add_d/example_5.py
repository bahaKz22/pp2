numbers = {1: 'one', 2: 'two'}
new_numbers = {k+2: v for k, v in numbers.items()}  # 3:'one', 4:'two'
numbers.update(new_numbers)
print(numbers)  # {1: 'one', 2: 'two', 3: 'one', 4: 'two'}
