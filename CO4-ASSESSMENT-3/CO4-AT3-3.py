# Ambiguity using CFG, PCFG and Neural Parsing

sentence = "She saw the man with a telescope"

print("Sentence:")
print(sentence)

# CFG
print("\n--- CFG ---")

print("Parse 1:")
print("She saw [the man with a telescope]")

print("Parse 2:")
print("She saw the man [with a telescope]")

print("CFG gives both possible structures.")


# PCFG
print("\n--- PCFG ---")

parse1 = 0.30
parse2 = 0.70

print("Parse 1 probability:", parse1)
print("Parse 2 probability:", parse2)

if parse1 > parse2:
    print("PCFG selects Parse 1")
else:
    print("PCFG selects Parse 2")


# Neural Parsing
print("\n--- NEURAL PARSING ---")

context = "She used a telescope to see the man."

print("Context:", context)

print("Neural parser uses context to select the meaning.")
print("Selected meaning:")
print("She used the telescope to see the man.")

print("\nConclusion:")
print("CFG -> generates possible parses")
print("PCFG -> selects using probabilities")
print("Neural -> uses context and learned patterns")
