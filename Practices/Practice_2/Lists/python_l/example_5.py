numbers = [1, 2, 3, 4, 5]
for n in numbers:
    print(n * 2)  # әр элементті 2-ге көбейтіп шығару

# Немесе индекспен
for i in range(len(numbers)):
    numbers[i] = numbers[i] ** 2
print(numbers)  # [1, 4, 9, 16, 25]
