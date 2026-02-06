a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)  # True (сол объекті)
print(a is c)  # False (элементтер бірдей, объекті әр түрлі)
print(5 is 5)  # True (Python integer caching)
print("abc" is "abc") # True (кейбір string literal кештеу)
print(a[0] is 1) # True (бір integer объекті)
