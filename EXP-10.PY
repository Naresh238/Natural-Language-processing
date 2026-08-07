words = ["I", "am", "playing", "cricket"]

# Initial tags
tags = ["NOUN", "NOUN", "NOUN", "NOUN"]

print("Before Transformation:")
for word, tag in zip(words, tags):
    print(word, "->", tag)

# Transformation rule:
# Words ending with "ing" are verbs
for i in range(len(words)):
    if words[i].endswith("ing"):
        tags[i] = "VERB"

print("\nAfter Transformation:")
for word, tag in zip(words, tags):
    print(word, "->", tag)