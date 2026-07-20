import re

# Input
reg_no = input("Enter Register Number: ")
email = input("Enter Institutional Email: ")
course = input("Enter Course Code: ")
semester = input("Enter Semester: ")
mobile = input("Enter Mobile Number: ")

status = True

# Register Number Validation (Example: 23AIDS001)
if re.fullmatch(r"\d{2}[A-Z]{4}\d{3}", reg_no):
    print("Register Number: Valid")
else:
    print("Register Number: Invalid")
    status = False

# Institutional Email Validation (Example: student@simats.edu.in)
if re.fullmatch(r"[a-zA-Z0-9._%+-]+@simats\.edu\.in", email):
    print("Email: Valid")
else:
    print("Email: Invalid")
    status = False

# Course Code Validation (Example: CS101)
if re.fullmatch(r"[A-Z]{2}\d{3}", course):
    print("Course Code: Valid")
else:
    print("Course Code: Invalid")
    status = False

# Semester Validation (1 to 8)
if re.fullmatch(r"[1-8]", semester):
    print("Semester: Valid")
else:
    print("Semester: Invalid")
    status = False

# Mobile Number Validation
if re.fullmatch(r"[6-9]\d{9}", mobile):
    print("Mobile Number: Valid")
else:
    print("Mobile Number: Invalid")
    status = False

# Final Report
print("\n----- Registration Status -----")
if status:
    print("Registration Successful")
else:
    print("Registration Failed")
