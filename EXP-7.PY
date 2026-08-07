text = "The boy is playing cricket"

words = text.split()

# Simple POS dictionary
pos = {
    "the": "DT",
    "boy": "NN",
    "is": "VB",
    "playing": "VBG",
    "cricket": "NN"
}

for word in words:
    tag = pos.get(word.lower(), "NN")
    print(word, "->", tag)