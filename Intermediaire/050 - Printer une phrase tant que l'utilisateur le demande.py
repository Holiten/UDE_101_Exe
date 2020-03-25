i = 0
continuer = "o"

while continuer == "o":
    print("Le compteur est maintenant à {}".format(i))
    continuer = input("Voulez vous continuer ? o/n ")
    i += 1
