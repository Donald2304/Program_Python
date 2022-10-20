def Eleve1():
    for x in range(1, 101):
        for y in range(1, 101):
            for z in range(101):
                if x<y<z:
                    if x**2+y**2==z**2:
                        print(x, y, z)

Eleve1()

