person = {"name": "Alice"}
person.setdefault("age", 25)   # қосылады, өйткені 'age' жоқ
person.setdefault("name", "Bob")  # өзгермейді, өйткені 'name' бар
print(person)  # {'name': 'Alice', 'age': 25}
