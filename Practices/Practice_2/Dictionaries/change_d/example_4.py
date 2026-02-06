person = {"name": "Alice"}
person.setdefault("age", 25)
person.setdefault("name", "Bob")  # бар элемент өзгермейді
print(person)  # {'name': 'Alice', 'age': 25}
