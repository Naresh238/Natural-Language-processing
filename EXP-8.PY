words = ["I", "eat", "apple"]

probability = {
    "I": {"PRON": 0.9, "NOUN": 0.1},
    "eat": {"VERB": 0.8, "NOUN": 0.2},
    "apple": {"NOUN": 0.9, "VERB": 0.1}
}

for word in words:
    tag = max(probability[word], key=probability[word].get)
    print(word, "->", tag)