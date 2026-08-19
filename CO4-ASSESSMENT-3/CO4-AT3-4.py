# Feature Structures and Subcategorization Frames

sentence = "The boy eats an apple"

print("Sentence:", sentence)

# Feature Structure
print("\n--- FEATURE STRUCTURE ---")

subject = {
    "word": "boy",
    "number": "singular",
    "person": "third"
}

verb = {
    "word": "eats",
    "number": "singular",
    "person": "third"
}

print("Subject:", subject)
print("Verb:", verb)

if (subject["number"] == verb["number"] and
        subject["person"] == verb["person"]):
    print("Subject-Verb Agreement: CORRECT")
else:
    print("Subject-Verb Agreement: INCORRECT")


# Subcategorization
print("\n--- SUBCATEGORIZATION ---")

print("Verb: eat")
print("Pattern: Subject + Verb + Object")

print("Subject:", "boy")
print("Verb:", "eats")
print("Object:", "apple")

print("\nSubcategorization:")
print("eat -> requires an object")

print("\nConclusion:")
print("Feature structures handle agreement.")
print("Subcategorization frames handle verb arguments.")
