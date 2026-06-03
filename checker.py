# Password Strength Checker - v5

special_chars = "!@#$%^&*"
password = input("Enter a password: ")

score = 0
feedback = []

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

print(f"\nPassword strength score: {score}/4")

if score == 4:
    print("Very strong password")
else:
    print("Improvements needed:")
    for tip in feedback:
        print("-", tip)