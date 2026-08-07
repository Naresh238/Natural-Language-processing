import re

text = "I am playing happily"

words = text.split()

for word in words:

    if re.match(r".*ing$", word):
        tag = "VERB"

    elif re.match(r".*ly$", word):
        tag = "ADVERB"

    elif word.lower() in ["I", "you", "he", "she", "we", "they"]:
        tag = "PRONOUN"

    else:
        tag = "NOUN"

    print(word, "->", tag)