scores = {"Alice": 85, "Bob": 90, "Charlie": 78, "David": 92}
for key in ["Bob", "David"]:
    scores.pop(key, None)  # key жоқ болса қате бермейді
print(scores)  # {'Alice': 85, 'Charlie': 78}
