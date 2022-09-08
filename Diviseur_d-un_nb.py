# Donner les diviseur d'un nombre

nb = int(input(">> "))

for d in range(1, nb):
    if nb % d == 0:
        print(d)