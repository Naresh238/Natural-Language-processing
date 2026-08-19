# Healthcare NLP System

sentence = (
    "The doctor who reviewed the patient last week "
    "recommends starting medication and scheduling "
    "a follow-up visit in Chennai."
)

print("========== HEALTHCARE NLP SYSTEM ==========")

# --------------------------------
# STEP 1: INPUT
# --------------------------------

print("\n1. INPUT:")
print(sentence)


# --------------------------------
# STEP 2: TOKENIZATION
# --------------------------------

words = sentence.replace(".", "").split()

print("\n2. TOKENS:")

for word in words:
    print(word)


# --------------------------------
# STEP 3: MEDICAL ENTITY RECOGNITION
# --------------------------------

entities = {
    "doctor": "Medical Professional",
    "patient": "Patient",
    "medication": "Treatment",
    "follow-up": "Medical Action",
    "visit": "Appointment",
    "Chennai": "Location"
}

print("\n3. MEDICAL ENTITIES:")

for entity, meaning in entities.items():
    print(entity, "->", meaning)


# --------------------------------
# STEP 4: FEATURE STRUCTURE
# --------------------------------

print("\n4. FEATURE STRUCTURE:")

subject = "doctor"
subject_number = "Singular"

verb = "recommends"
verb_number = "Singular"

print("Subject:", subject)
print("Subject Number:", subject_number)
print("Verb:", verb)
print("Verb Number:", verb_number)

if subject_number == verb_number:
    print("Agreement: CORRECT")
else:
    print("Agreement: INCORRECT")


# --------------------------------
# STEP 5: MEDICAL ACTIONS
# --------------------------------

actions = {
    "reviewed": "Doctor reviews Patient",
    "recommends": "Doctor recommends Treatment/Action",
    "starting medication": "Start Medication",
    "scheduling follow-up visit": "Schedule Follow-up Visit"
}

print("\n5. MEDICAL ACTIONS:")

for action, meaning in actions.items():
    print(action, "->", meaning)


# --------------------------------
# STEP 6: SUB-CATEGORIZATION
# --------------------------------

print("\n6. SUB-CATEGORIZATION FRAMES:")

frames = {
    "review": "Doctor + reviews + Patient",
    "recommend": "Doctor + recommends + Treatment",
    "start": "Patient + starts + Medication",
    "schedule": "Hospital + schedules + Follow-up Visit"
}

for verb, frame in frames.items():
    print(verb, ":", frame)


# --------------------------------
# STEP 7: PCFG
# --------------------------------

print("\n7. PCFG:")

parse1 = 0.75
parse2 = 0.25

print("Parse 1 Probability:", parse1)
print("Parse 2 Probability:", parse2)

if parse1 > parse2:
    print("Best Parse: Parse 1")
else:
    print("Best Parse: Parse 2")


# --------------------------------
# STEP 8: STRUCTURED OUTPUT
# --------------------------------

print("\n8. STRUCTURED OUTPUT:")

print("Subject  : Doctor")
print("Patient  : Patient")
print("Action 1 : Start Medication")
print("Action 2 : Schedule Follow-up Visit")
print("Location : Chennai")


# --------------------------------
# FINAL
# --------------------------------

print("\n========== FINAL RESULT ==========")
print("Diagnosis  : Not explicitly mentioned")
print("Treatment  : Medication")
print("Follow-up  : Follow-up Visit")
print("Location   : Chennai")
