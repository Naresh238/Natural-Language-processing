# Morphological Analysis without NLTK

word = input("Enter a word: ").lower()

print("Original Word :", word)

# Check Prefix
if word.startswith("un"):
    print("Prefix :", "un")
    word = word[2:]

elif word.startswith("re"):
    print("Prefix :", "re")
    word = word[2:]

elif word.startswith("dis"):
    print("Prefix :", "dis")
    word = word[3:]

# Check Suffix
if word.endswith("ing"):
    print("Suffix :", "ing")
    root = word[:-3]

elif word.endswith("ed"):
    print("Suffix :", "ed")
    root = word[:-2]

elif word.endswith("ly"):
    print("Suffix :", "ly")
    root = word[:-2]

elif word.endswith("s"):
    print("Suffix :", "s")
    root = word[:-1]

else:
    root = word

print("Root Word :", root)
