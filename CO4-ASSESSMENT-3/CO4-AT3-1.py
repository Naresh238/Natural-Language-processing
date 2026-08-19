# CFG Tree vs Dependency Parsing

sentence = "The boy eats an apple"

print("Sentence:", sentence)

# CFG representation
print("\nCFG Tree:")
print("S")
print("|-- NP")
print("|   |-- The")
print("|   |-- boy")
print("|")
print("|-- VP")
print("    |-- eats")
print("    |-- NP")
print("        |-- an")
print("        |-- apple")

# Dependency representation
print("\nDependency Parsing:")
print("eats -> boy       (subject)")
print("eats -> apple     (object)")
print("boy -> The        (determiner)")
print("apple -> an       (determiner)")

print("\nConclusion:")
print("CFG shows phrase structure.")
print("Dependency parsing shows word-to-word relationships.")
