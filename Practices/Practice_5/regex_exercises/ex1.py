import re

strings = ["a", "ab", "abb", "b", "ba", "aa", "abbb"]

for s in strings:
    if re.fullmatch(r"a[b]*", s):
        print(f"Matched: {s}")
print()
for d in strings:
    if re.match(r"a[b]*", d):
        print(f"Matched: {d}")
print()
for a in strings:
    if re.search(r"a[b]*", a):
        print(f"Matched: {a}")
