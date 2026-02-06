original = {"student": {"name": "Alice", "age": 25}}
copy_dict = original.copy()
original["student"]["age"] = 26
print(copy_dict)  # {'student': {'name': 'Alice', 'age': 26}} → ішкі dict өзгерді
