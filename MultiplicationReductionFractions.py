# Multiplier puis reduire deux fractions

n1 = int(input("Numerateur 1 >> "))
d1 = int(input("Denominateur 1 >> "))

n2 = int(input("Numerateur 2 >> "))
d2 = int(input("Denominateur 2 >> "))

n3 = n1 * n2
d3 = d1 * d2

liste = []

for a in range(1, n3 + 1):
    if d3 % a == 0 and n3 % a == 0:
        liste.append(a)

liste = max(liste)

n3 = n3/liste
d3 = d3/liste

print("Numerateur >>", n3)
print("Denominateur >>", d3)

