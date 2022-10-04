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

print(str(ax), '+('+str(b)+')','=', str(c),'+('+str(d)+')')
