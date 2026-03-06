import re

strings = "Python, is. fun,nice."

new = re.sub(r"[ \,\.]",":",strings)

print(new)