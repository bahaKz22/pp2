words = ["cat", "lion", "tiger", "dog"]

# Sort by length of word
sorted_words = sorted(words, key=lambda x: len(x))

print(sorted_words)  
# Output: ['cat', 'dog', 'lion', 'tiger']