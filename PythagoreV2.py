# Savoir si un triangle est rectangle #2

import random

while True:
    v1 = int(input(">> "))
    v2 = int(input(">> "))
    v3 = int(input(">> "))

    Nombres = [v1, v2, v3]
    Nombres.sort()



    if Nombres[0] ** 2 + Nombres[1] ** 2 == Nombres[2] ** 2:
        print("Le triangle est rectangle")
    else:
        print("Le triangle n'est pas rectangle ")
