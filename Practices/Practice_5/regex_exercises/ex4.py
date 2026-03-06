import re

strings = ["Hello","hello","hELLO","Abc"]

for s in strings:
    if re.fullmatch(r"[A-Z][a-z]+",s):
        print(f"matched: {s}")

str = "Hello my name is Bagdaulet"
d = re.findall(r"[A-Z][a-z]+",str)
print(d)