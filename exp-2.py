<<<<<<< HEAD
import re

# Product List
products = [
    "Python Book",
    "Java Programming",
    "SQL Guide",
    "Machine Learning",
    "NLP Toolkit",
    "Python Notebook",
    "Java Book",
    "Learning Python",
    "SQL Database",
    "Python IDE"
]

keyword = input("Enter search keyword: ")

# Exact Search
exact = []
for product in products:
    if re.fullmatch(keyword, product, re.IGNORECASE):
        exact.append(product)

# Prefix Search
prefix = []
for product in products:
    if re.match(keyword, product, re.IGNORECASE):
        prefix.append(product)

# Suffix Search
suffix = []
for product in products:
    if re.search(keyword + "$", product, re.IGNORECASE):
        suffix.append(product)

# Partial Search
partial = []
for product in products:
    if re.search(keyword, product, re.IGNORECASE):
        partial.append(product)

# Display Results
print("\nExact Search:")
for p in exact:
    print(p)
print("Total Matches:", len(exact))

print("\nPrefix Search:")
for p in prefix:
    print(p)
print("Total Matches:", len(prefix))

print("\nSuffix Search:")
for p in suffix:
    print(p)
print("Total Matches:", len(suffix))

print("\nPartial Search:")
for p in partial:
    print(p)
print("Total Matches:", len(partial))
=======
import re

# Product List
products = [
    "Python Book",
    "Java Programming",
    "SQL Guide",
    "Machine Learning",
    "NLP Toolkit",
    "Python Notebook",
    "Java Book",
    "Learning Python",
    "SQL Database",
    "Python IDE"
]

keyword = input("Enter search keyword: ")

# Exact Search
exact = []
for product in products:
    if re.fullmatch(keyword, product, re.IGNORECASE):
        exact.append(product)

# Prefix Search
prefix = []
for product in products:
    if re.match(keyword, product, re.IGNORECASE):
        prefix.append(product)

# Suffix Search
suffix = []
for product in products:
    if re.search(keyword + "$", product, re.IGNORECASE):
        suffix.append(product)

# Partial Search
partial = []
for product in products:
    if re.search(keyword, product, re.IGNORECASE):
        partial.append(product)

# Display Results
print("\nExact Search:")
for p in exact:
    print(p)
print("Total Matches:", len(exact))

print("\nPrefix Search:")
for p in prefix:
    print(p)
print("Total Matches:", len(prefix))

print("\nSuffix Search:")
for p in suffix:
    print(p)
print("Total Matches:", len(suffix))

print("\nPartial Search:")
for p in partial:
    print(p)
print("Total Matches:", len(partial))
>>>>>>> 2d87fcbe31b843eac44fa4ce07aedbf0e761ab99
