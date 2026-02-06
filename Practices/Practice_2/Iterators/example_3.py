import itertools

counter = itertools.count(1)
for i in counter:
    print(i)
    if i == 5:
        break
