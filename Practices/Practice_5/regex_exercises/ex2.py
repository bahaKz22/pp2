import re

strings = ["a","ab","abb","abbb","abbbb","abbbx"]

for s in strings:
    if re.fullmatch(r"a[b]{2,3}", s):
        print(f"Matched: {s}")
print()