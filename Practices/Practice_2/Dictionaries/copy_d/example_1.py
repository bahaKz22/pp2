person = {"name": "Alice", "age": 25}
person_copy = person.copy()
print(person_copy)  # {'name': 'Alice', 'age': 25}

# түпнұсқаға өзгеріс қосқанда көшірме өзгермейді
person["age"] = 26
print(person_copy)  # {'name': 'Alice', 'age': 25}
