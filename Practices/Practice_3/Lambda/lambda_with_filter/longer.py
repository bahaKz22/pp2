words = ["cat", "lion", "dog", "tiger"]

# Filter words with length > 3
long_words = list(filter(lambda x: len(x) > 3, words))

print(long_words)  # Output: ['lion', 'tiger']