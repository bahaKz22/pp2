people = [("Ali", 25), ("Sara", 20), ("John", 30)]

# Sort by age (second value in tuple) using lambda
sorted_people = sorted(people, key=lambda x: x[1])

print(sorted_people)  
# Output: [('Sara', 20), ('Ali', 25), ('John', 30)]