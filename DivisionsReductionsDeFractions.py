# Diviser puis reduire deux fractions

n1 = int(input("Numerateur 1 >> "))
d1 = int(input("Denominateur 1 >> "))

n2 = int(input("Numerateur 2 >> "))
d2 = int(input("Denominateur 2 >> "))

ResultN = n1 * d2 
ResultD = d1 * n2

print(" ")        # Espace dans le terminal pour que plus lisible

Reductions = []

for a in range(1, ResultN + 1):
    if ResultD % a == 0 and ResultN % a == 0:
        Reductions.append(a)

ResultN = ResultN / max(Reductions)
ResultD = ResultD / max(Reductions)

print(ResultN)
print(ResultD)


