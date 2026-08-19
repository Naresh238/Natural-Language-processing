# Top-Down Parsing vs Earley Parsing

sentence = "Book a flight to Delhi"

print("Input:", sentence)

# Top-Down Parsing
print("\n--- TOP-DOWN PARSING ---")

print("Start with S")
print("S -> VP")
print("VP -> Verb NP")
print("Verb -> Book")
print("NP -> a flight to Delhi")

print("\nProblem:")
print("Top-down parsing may require backtracking.")
print("It is difficult with incomplete input.")


# Earley Parsing
print("\n--- EARLEY PARSING ---")

words = sentence.split()

chart = []

for word in words:
    chart.append(word)

print("Processed words:")

for word in chart:
    print(word)

print("\nEarley advantages:")
print("1. Handles ambiguity")
print("2. Handles incomplete input")
print("3. Stores partial parsing results")
print("4. Suitable for dynamic input")

print("\nConclusion:")
print("Earley parsing is better for real-time dynamic input.")
