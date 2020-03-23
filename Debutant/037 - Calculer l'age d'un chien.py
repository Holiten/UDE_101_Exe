age = int(input("Entrer l'age du chien : "))

if age < 0:
    print("Vous devez entrer un age positif :")
    exit()
elif age <= 2:
    d_age = age * 10.5
else:
    d_age = 21 + (age - 2) * 4

print("L'age du chien en age humain est {} ans".format(d_age))
