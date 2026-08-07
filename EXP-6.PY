import random

text = "I like Python. I like machine learning. Python is easy."

words = text.lower().replace(".", "").split()

bigrams = []
for i in range(len(words) - 1):
    bigrams.append((words[i], words[i + 1]))

print("Bigrams:")
print(bigrams)

print("\nGenerated Text:")

word = "i"
result = [word]

for i in range(5):
    next_words = [b for a, b in bigrams if a == word]

    if next_words:
        word = random.choice(next_words)
        result.append(word)
    else:
        break

print(" ".join(result))