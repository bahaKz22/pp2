letters = ("a", "b", "c")
letters = letters[:1] + ("x",) + letters[2:]
print(letters)  # ('a', 'x', 'c')
