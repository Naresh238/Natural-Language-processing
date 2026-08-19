# Semantic Representation in Customer Support Chatbot

queries = {
    "Q1": ("Activate Roaming", "Activate Roaming"),
    "Q2": ("Deactivate Caller Tune", "Activate Caller Tune"),
    "Q3": ("Query Data Balance", "Query Data Balance"),
    "Q4": ("Activate 5G Service", "Activate 5G Service")
}

correct = 0

for q, values in queries.items():
    actual = values[0]
    predicted = values[1]

    print(q)
    print("Actual Intent    :", actual)
    print("Predicted Intent :", predicted)

    if actual == predicted:
        print("Result: Correct\n")
        correct += 1
    else:
        print("Result: Incorrect\n")

accuracy = (correct / len(queries)) * 100

print("Total Correct:", correct)
print("Accuracy:", accuracy, "%")
