# Password Strength Checker - v1

password = input("Entrez un mot de passe : ")

if len(password) < 8:
    print(" Mot de passe trop court")
else:
    print(" Longueur correcte")