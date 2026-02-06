a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))                 # {1, 2, 3, 4, 5}
print(a.intersection(b))          # {3}
print(a.difference(b))            # {1, 2}
print(a.symmetric_difference(b))  # {1, 2, 4, 5}
