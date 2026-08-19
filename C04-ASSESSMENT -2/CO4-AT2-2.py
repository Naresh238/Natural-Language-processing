# Voice Assistant Parsing

sentence = "Book a flight to Delhi with a window seat"

words = sentence.split()

print("Input:")
print(sentence)

# -----------------------------
# TOP-DOWN PARSING
# -----------------------------

print("\n--- TOP-DOWN PARSING ---")

print("Start from S")
print("S -> VP")
print("VP -> Verb NP")
print("Verb -> Book")
print("NP -> Det N PP")

print("\nTop-Down Parser:")
print("Book -> Verb")
print("a flight -> Noun Phrase")
print("to Delhi -> Prepositional Phrase")
print("with a window seat -> Prepositional Phrase")

print("\nProblem:")
print("Top-down parser may try different rules.")
print("This can cause backtracking for ambiguous sentences.")


# -----------------------------
# EARLEY PARSING
# -----------------------------

print("\n--- EARLEY PARSING ---")

chart = []

for i, word in enumerate(words):
    state = "Processed: " + word
    chart.append(state)

print("\nEarley Chart:")

for i, state in enumerate(chart):
    print("State", i, ":", state)

print("\nEarley Parser:")
print("Stores partial parsing results.")
print("Handles ambiguity better.")
print("Can process incomplete input.")
print("Suitable for voice assistants.")

# Final meaning
print("\nFinal Interpretation:")
print("Book a flight to Delhi with a window seat.")
