# Transition-Based vs Graph-Based Dependency Parsing

sentence = "The boy eats an apple"

words = sentence.split()

print("Sentence:", sentence)

# --------------------------------
# TRANSITION-BASED PARSING
# --------------------------------

print("\n--- TRANSITION-BASED PARSING ---")

stack = ["ROOT"]
buffer = words.copy()

while buffer:
    word = buffer.pop(0)
    stack.append(word)

    print("Stack:", stack)
    print("Buffer:", buffer)

print("\nTransition-based parser:")
print("Uses a sequence of decisions.")
print("Usually fast and efficient.")


# --------------------------------
# GRAPH-BASED PARSING
# --------------------------------

print("\n--- GRAPH-BASED PARSING ---")

print("Possible dependency edges:")

print("eats -> boy     (subject)")
print("eats -> apple   (object)")
print("boy -> The      (determiner)")
print("apple -> an     (determiner)")

print("\nGraph-based parser:")
print("Creates possible dependency relationships.")
print("Searches for the best dependency tree.")


# --------------------------------
# COMPARISON
# --------------------------------

print("\n--- COMPARISON ---")

print("Transition-based:")
print("Fast")
print("Low memory")
print("Good for large datasets")

print("\nGraph-based:")
print("More global analysis")
print("Usually more computationally expensive")
print("Can provide accurate dependency structures")

print("\nConclusion:")
print("Transition-based parsing is suitable for large-scale applications.")
