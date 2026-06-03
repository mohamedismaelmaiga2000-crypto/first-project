# Password Strength Checker - v3

password = input("Enter a password: ")

errors = []

if len(password) < 8:
    errors.append("Password too short (minimum 8 characters)")

if not any(char.isupper() for char in password):
    errors.append("Add at least one uppercase letter")

if not any(char.isdigit() for char in password):
    errors.append("Add at least one number")

if errors:
    print("Weak password:")
    for error in errors:
        print("-", error)
else:
    print("Strong password")