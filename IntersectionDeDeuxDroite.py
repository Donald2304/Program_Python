import random

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

userRepNumerateur = input("")# try , except jusqua ce que la reponse donne soit un chiffres ou un nombre

print(str(ax)+"x", '+('+str(b)+')','=', str(c)+"x",'+('+str(d)+')')
print(str(ax-c)+"x","=",str(d-b))
print("x =",str(d-b)+"/"+str(ax-c))
