import random
afficheResultatN = 0
afficheResultatD = 0
afficheResultat = 0
listeChiffres = list(range(-10, 10 + 1))
listeChiffres.remove(0)

print("ax + b = cx + d")
print("x(a-c) = d - b")
print("x = (d-b) / (a-c)")
print('')

ax= random.choice(listeChiffres)
b = random.choice(listeChiffres)
c = random.choice(listeChiffres)
d = random.choice(listeChiffres)

print("Resoudre :")
print(str(ax)+"x", '+('+str(b)+')','=', str(c)+"x",'+('+str(d)+')')
print("")

while afficheResultat == 0:
    try:
        userRepNumerateur = float(input("x = ?/ : "))
        if userRepNumerateur == float(userRepNumerateur):
            afficheResultatN = 1
    except ValueError:
        print("Ce n'est pas un nombre")
        continue

    while afficheResultat == 0: 
        if afficheResultatN == 1:
            try:
                userRepDenominateur = float(input("x = " + str(userRepNumerateur) + " /? : "))
                if userRepDenominateur == float(userRepDenominateur):
                    afficheResultat = 1
            except ValueError:
                print("Ce n'est pas un nombre")
print("Votre reponse : x = " + str(userRepNumerateur) + " / " + str(userRepDenominateur))

if d-b == userRepNumerateur and ax-c == userRepDenominateur:
    print("Votre reponse est juste")
else:
    print("")
    print("Faux la reponse est:")
    print(str(ax-c)+"x","=",str(d-b))
    print("x =",str(d-b)+"/"+str(ax-c))


