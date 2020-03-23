prenom = "Pierre"

if prenom == str(prenom):
    print("La variable est une chaîne de caractères")

prenom = 0

if prenom != str(prenom):
    pass

prenom = "Pierre"
if type(prenom) == str:
    print("La variable est une chaîne de caractères")

prenom = 0

if isinstance(prenom, str):
    print("La variable est une chaîne de caractères")