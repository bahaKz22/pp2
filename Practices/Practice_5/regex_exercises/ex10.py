import re

strings = "HelloWorldBaga"

s = re.findall(r"[A-Z][a-z]*", strings)
snake = '_'.join(word.lower() for word in s)
print(snake)