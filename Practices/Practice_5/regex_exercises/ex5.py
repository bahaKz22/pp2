import re

strings = ["ab", "acb", "a123b", "acdeb", "abc", "ba", "a_b"]

for s in strings:
    if re.fullmatch(r"a.*b",s):
        print(f"Matched: {s}")
print()
for d in strings:
    if re.search(r"a.*b",s):
        print(f"Matched: {d}")
