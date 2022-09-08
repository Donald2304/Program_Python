# Savoir si un triangle est rectangle

while True:
    v1 = int(input("Plus petite valeur >> "))
    v2 = int(input("Valeur moyenne >> "))
    v3 = int(input("Plus grande valeur >> "))

    if v1 ** 2 + v2 ** 2 == v3 ** 2:
        print("Le triangle est rectangle")
    else:
        print("Le triangle n'est pas rectangle ")

