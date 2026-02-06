letters = {"a", "b", "c"}
letters.remove("b")   # элемент жоқ болса KeyError
letters.discard("x")  # элемент жоқ болса қате жоқ
print(letters)        # {'a', 'c'}
