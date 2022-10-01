class Couleur:
    Bleu = '\033[94m' 
    Rouge = '\033[91m' 
    Normal = '\033[0m'
    Blanc = '\033[97m' 
    Noire = '\033[30m'
    Vert = '\033[32m'
    Orange = '\033[33m'
    Jaune = '\033[93m'
    Violet = '\033[95m'

# Coordonné point A( ; )
PasseOrdonneA = 0
while PasseOrdonneA == 0 :
    try:
        PointAa = int(input("A(?, ): ")) 
        if PointAa == int(PointAa):
            PasseOrdonneA = 1
    except ValueError:
        print(Couleur.Rouge + 'IL FAUT ENTRER UN NUMERO' + Couleur.Normal)

PasseAbscisseB = 0
while PasseAbscisseB == 0:
    try:
        PointAo = int(input('A( ;?)'))
        if PointAo == int(PointAo):
            PasseAbscisseB = 1
    except ValueError:
        print(Couleur.Rouge + "IL FAUT UN NUMERO" + Couleur.Normal)

print('A(' + str(PointAa) + ';' + str(PointAo) + ')')

# Coordonné point B( ; )
PasseOrdonneB = 0
while PasseOrdonneB == 0:
    try:
        PointBa = int(input('B(?; )'))
        if PointBa == int(PointBa):
            PasseOrdonneB = 1
    except ValueError:
        print(Couleur.Rouge + 'IL FAUT UN NUMERO' + Couleur.Normal)
