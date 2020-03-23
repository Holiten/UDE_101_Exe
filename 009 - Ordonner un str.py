chaine = "Pierre, Julien, Anne, Marie, Lucien"

chaine_list = chaine.split(", ")
print(chaine_list)
chaine_list.sort()
print(chaine_list)
chaine_orde = ", ".join(chaine_list)
print(chaine_orde)