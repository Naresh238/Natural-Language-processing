# Regular Expression Example

import re

text = "My phone number is 9876543210"

# Search for a 10-digit number
pattern = r"\d{10}"

result = re.search(pattern, text)

if result:
    print("Phone Number Found:", result.group())
else:
    print("Phone Number Not Found")
