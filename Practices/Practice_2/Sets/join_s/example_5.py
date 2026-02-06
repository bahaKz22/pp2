set1 = {1, 2, 3}
set2 = {4, 5, 6}
combined = {x for x in set1} | {y for y in set2}
print(combined)  # {1, 2, 3, 4, 5, 6}
