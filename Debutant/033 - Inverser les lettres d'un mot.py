mot = "Udemy"

resultat = []

for lettre in reversed(mot):
    resultat.append(lettre)

resultat_format = "".join(resultat)
print(resultat_format.capitalize())
