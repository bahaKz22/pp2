t = (1, 2, 3)
lst = list(t)   # tuple → list
lst.append(4)   # list-ке элемент қосу
t = tuple(lst)  # list → tuple қайта айналдыру
print(t)        # (1, 2, 3, 4)
