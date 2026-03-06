import re

strings = "Hello_world"
parts = strings.split("_")

for d in parts[1:]:
    print(d.capitalize())