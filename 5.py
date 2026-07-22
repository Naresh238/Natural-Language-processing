# Simple Word Stemming without NLTK

words = ["playing", "running", "studies", "happiness", "cats"]

print("Original Word\tStemmed Word")
print("-" * 30)

for word in words:
    stem = word

    if stem.endswith("ing"):
        stem = stem[:-3]
    elif stem.endswith("ies"):
        stem = stem[:-3] + "y"
    elif stem.endswith("ness"):
        stem = stem[:-4]
    elif stem.endswith("ed"):
        stem = stem[:-2]
    elif stem.endswith("s"):
        stem = stem[:-1]

    print(word, "\t\t", stem)
