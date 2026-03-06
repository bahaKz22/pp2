import re
strings = "HelloWorldBaga"
s = re.findall(r"[A-Z][a-z]*", strings)
join = ' '.join(s)
print(join)