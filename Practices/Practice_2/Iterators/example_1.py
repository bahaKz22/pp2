fruits = ["apple", "banana", "cherry"]
it = iter(fruits)  # iterator жасау

print(next(it))  # apple
print(next(it))  # banana
print(next(it))  # cherry
# print(next(it))  # StopIteration қате береді
