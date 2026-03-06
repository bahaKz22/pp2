import re
strings = "MyNameIsBagdaulet"
w = re.findall(r"[A-Z][a-z]*",strings)
print(w)