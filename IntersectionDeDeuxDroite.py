import random
afficheResultatN = 0
afficheResultatD = 0
afficheResultat = 0
reductionUser = []
reductionOrdinateur = []
userRepNumerateur2 = None
userRepDenominateur2 = None
listeChiffres = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


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
        userRepNumerateur = int(input("x = ?/ : "))
        if userRepNumerateur == int(userRepNumerateur):
            afficheResultatN = 1
    except ValueError:
        print("Ce n'est pas un nombre")
        continue

    while afficheResultat == 0: 
        if afficheResultatN == 1:
            try:
                userRepDenominateur = int(input("x = " + str(userRepNumerateur) + " /? : "))
                if userRepDenominateur == int(userRepDenominateur):
                    afficheResultat = 1
            except ValueError:
                print("Ce n'est pas un nombre")
print("Votre reponse : x = " + str(userRepNumerateur) + " / " + str(userRepDenominateur))

N = userRepNumerateur / (d-b)
D = userRepDenominateur / (ax-c) 
if N == D:
    userRepNumerateur2 = userRepNumerateur
    userRepDenominateur2 = userRepDenominateur

    userRepNumerateur2 /= N
    userRepDenominateur2 /= D

if d-b == userRepNumerateur and ax-c == userRepDenominateur or d-b == userRepNumerateur2 and ax-c == userRepDenominateur2:
    print("Votre reponse est juste")
    if d-b == userRepNumerateur2 and ax-c == userRepDenominateur2:
        print("Mais elle peut être simplifier")
        print(str(userRepNumerateur2/N) + " / " + str(userRepDenominateur2/D))
    else:
        pass
else:
    for a in listeChiffres:
        if (d-b) % a == 0 and (ax-c) % a == 0:
            reductionOrdinateur.append(a)
    repN = d-b
    repN /= max(reductionOrdinateur)
    repD = ax-c
    repD /= max(reductionOrdinateur)

    print("")
    print("Faux la reponse est:")
    print(str(ax)+"x", '+('+str(b)+')','=', str(c)+"x",'+('+str(d)+')')
    print(str(ax-c)+"x","=",str(d-b))
    print("x =",str(repN)+"/"+str(repD))


