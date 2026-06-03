# Password Strength Checker - v7
# Secure password input + hashing

import hashlib
import getpass

special_chars = "!@#$%^&*"

# Secure input (hidden)
password = getpass.getpass("Enter a password (hidden input): ")

score = 0
feedback = []

# Strength checks
if len(password) >= 8:
    score += 1
else:
    feedback.append("Minimum 8 characters")

if any(char.isupper() for char in password):
    score += 1
else:
    feedback.append("Add an uppercase letter")

if any(char.isdigit() for char in password):
    score += 1
else:
    feedback.append("Add a number")

if any(char in special_chars for char in password):
    score += 1
else:
    feedback.append("Add a special character")

# Hashing
hashed_password = hashlib.sha256(password.encode()).hexdigest()

print(f"\nPassword strength score: {score}/4")

if score == 4:
    print("Strong password")
else:
    print("Improvements needed:")
    for tip in feedback:
        print("-", tip)

print("\nHashed password (SHA-256):")
print(hashed_password)