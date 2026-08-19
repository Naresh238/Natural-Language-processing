# Banking Chatbot using simple CFG idea

sentence = "Show me the transactions with the card from last month"

words = sentence.split()

print("Input Sentence:")
print(sentence)

print("\nWords:")
for word in words:
    print(word)

# Simple grammar rules
grammar = {
    "S": ["VP"],
    "VP": ["V NP"],
    "NP": ["Det N PP", "Det N PP PP"],
    "PP": ["P NP"]
}

print("\nCFG Rules:")
for key, value in grammar.items():
    print(key, "->", " | ".join(value))

# Find ambiguity
print("\nAmbiguity:")
print("The phrase 'with the card' can describe the transactions.")
print("The phrase 'from last month' gives the time information.")

print("\nPossible Meaning 1:")
print("Show transactions made with the card during last month.")

print("\nPossible Meaning 2:")
print("Show transactions related to a card from last month.")

# PCFG idea
probability1 = 0.80
probability2 = 0.20

print("\nPCFG Probabilities:")
print("Meaning 1:", probability1)
print("Meaning 2:", probability2)

if probability1 > probability2:
    print("Selected Meaning: Transactions made with the card last month")
else:
    print("Selected Meaning: Card from last month")
