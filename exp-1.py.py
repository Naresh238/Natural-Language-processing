<<<<<<< HEAD
import re

# Sample Resume
resume = """
Name: Naresh Reddy Paluri
Email: naresh@gmail.com
Phone: 9876543210
Skills: Python, Java, SQL, Machine Learning, NLP
Experience: 3 years
"""

# Extract Name
name = re.search(r"Name:\s*(.*)", resume)
if name:
    name = name.group(1)
else:
    name = "Not Found"

# Extract Email
email = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", resume)

# Extract Mobile Number
phone = re.findall(r"\b\d{10}\b", resume)

# Extract Skills
skills_list = ["Python", "Java", "SQL", "Machine Learning", "NLP"]
skills_found = []

for skill in skills_list:
    if re.search(skill, resume, re.IGNORECASE):
        skills_found.append(skill)

# Extract Experience
experience = re.search(r"(\d+)\s+years?", resume, re.IGNORECASE)

if experience:
    years = int(experience.group(1))
else:
    years = 0

# Display Summary
print("----- Candidate Profile -----")
print("Name:", name)
print("Email:", email)
print("Phone:", phone)
print("Skills:", skills_found)
print("Experience:", years, "Years")

# Eligibility Check
if years >= 2 and "Python" in skills_found:
    print("\nStatus: Eligible for Shortlisting")
else:
    print("\nStatus: Not Eligible")
=======
import re

# Sample Resume
resume = """
Name: Naresh Reddy Paluri
Email: naresh@gmail.com
Phone: 9876543210
Skills: Python, Java, SQL, Machine Learning, NLP
Experience: 3 years
"""

# Extract Name
name = re.search(r"Name:\s*(.*)", resume)
if name:
    name = name.group(1)
else:
    name = "Not Found"

# Extract Email
email = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", resume)

# Extract Mobile Number
phone = re.findall(r"\b\d{10}\b", resume)

# Extract Skills
skills_list = ["Python", "Java", "SQL", "Machine Learning", "NLP"]
skills_found = []

for skill in skills_list:
    if re.search(skill, resume, re.IGNORECASE):
        skills_found.append(skill)

# Extract Experience
experience = re.search(r"(\d+)\s+years?", resume, re.IGNORECASE)

if experience:
    years = int(experience.group(1))
else:
    years = 0

# Display Summary
print("----- Candidate Profile -----")
print("Name:", name)
print("Email:", email)
print("Phone:", phone)
print("Skills:", skills_found)
print("Experience:", years, "Years")

# Eligibility Check
if years >= 2 and "Python" in skills_found:
    print("\nStatus: Eligible for Shortlisting")
else:
    print("\nStatus: Not Eligible")
>>>>>>> 2d87fcbe31b843eac44fa4ce07aedbf0e761ab99
