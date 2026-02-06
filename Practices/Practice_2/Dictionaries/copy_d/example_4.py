import copy

original = {"student": {"name": "Alice", "age": 25}}
copy_dict = copy.deepcopy(original)
original["student"]["age"] = 26
print(copy_dict)  # {'student': {'name': 'Alice', 'age': 25}} → nested dict өзгермеді
