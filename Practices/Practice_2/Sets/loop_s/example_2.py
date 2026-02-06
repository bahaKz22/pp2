numbers = {1, 2, 3, 4}
it = iter(numbers)
while True:
    try:
        print(next(it))
    except StopIteration:
        break
