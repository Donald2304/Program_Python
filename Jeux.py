
import time,random
listeCalcule = list(range(-50 , 50+1))
cagnotte = 0

def Espace(pause,Inferieur):
    espace2 = ""
    nbEspace2 = 0
    time.sleep(pause)
    while nbEspace2 < Inferieur:
        print("")
        espace2 += " "
        nbEspace2 += 1

def AfficheCagnotte():
    print("Vous avez " + str(cagnotte) + "€")

def Calcule():
    global cagnotte
    nombre1 = random.choice(listeCalcule)
    nombre2 = random.choice(listeAleatoire)
    print(nombre1, "+", nombre2)
    reponseOrdinateur = nombre1 + nombre2
    reponse = input("Reponse = ")
    if int(reponse) == reponseOrdinateur:
        print("Juste")
        cagnotte += 100
        Espace(3, 100)
        AfficheCagnotte()
    elif int(reponse) != reponseOrdinateur:
        print("Faux")
    
class Couleur:
    Bleu = '\033[94m' 
    Rouge = '\033[91m' 
    Normal = '\033[0m'
    Violet = '\033[95m'
    Blanc = '\033[97m' 
    Noire = '\033[30m'
    Vert = '\033[32m'
    Orange = '\033[33m'
    Cyan = '\033[36m'
    Gris = '\033[90m'               # Utiliser
    RougeClair = '\033[91m'
    VertClair = '\033[92m'
    Jaune = '\033[93m'              # Utiliser
    Rose = '\033[95m'
    CyanClair = '\033[96m'

# Pour animation du debut

Debut = 0
espace = ""
nbEspace = 0
a = 0
barre = "-"
nbBarre = 0
Suite = 0
EcranHauteur = 0
Lancement = 0

while Debut == 0:
    try:
        Lanceur = str(input("Lancer le jeu(j) = "))
        if Lanceur == "j":
            Debut = 1
    except SyntaxWarning:
        ...

while Suite == 0:
    while a < 25:
        print('')
        a +=1
    if nbEspace > 205:
        espace = ""
        nbEspace = 0
        Suite = 1
    if nbBarre > 205:
        barre =  "-"
        Suite = 1
        nbBarre = 0
    espace += " "
    barre += "-"
    nbBarre += 1
    nbEspace += 1
    
    if Suite == 0:
        while Lancement < 40:
            print("")
            Lancement += 1
        Lancement = 0

        time.sleep(0.1)
        print(Couleur.Jaune + "       ____")
        print(                "      |    |")
        print(                "      |____|"+ Couleur.Normal)
        print(Couleur.Gris+" _______ ___ _____   __          __ ___ _ ________ __ _ __________ ______ ____ _ _ ___ __ _ _ _ __ _ __ __   ___________      ________ __    ___ _ __ _ __ _ __ _____ _ ________________   __ _ ______ __ ___ _______   __ ______ __")
        print("_______ __________      _______    ____     _ _ _______ __ ____ _          ________ _ _ _ ______ _ ________ __ __ __ ___           ___ _  _ _ ____ ___ __ __ ______ __ ___ _________ ______ __ __ __ __     __ _ __    _ _ _ _______ " + Couleur.Normal)


        while Lancement < 7:
            print("")
            Lancement += 1
        Lancement = 0

        print(espace + Couleur.Vert + "   _______")
        print(espace +                "  / || || \__")
        print(espace +                "   O---------O" + Couleur.Normal)
        print(Couleur.Jaune + "----------------------"+barre) 

while Lancement < 100:
    print("")
    Lancement += 1
Lancement = 0

print(Couleur.Normal + "DEBUT DU JEU ....")
time.sleep(3)

while Lancement < 100:
    print("")
    Lancement += 1
Lancement = 0

print("Chargement en cours 20%")
time.sleep(1.5)

while Lancement < 100:
    print("")
    Lancement += 1
Lancement = 0
print("Chargement en cours 40%")
time.sleep(1.5)

while Lancement < 100:
    print("")
    Lancement += 1
Lancement = 0
print("Chargement en cours 60%")
time.sleep(1.5)

while Lancement < 100:
    print("")
    Lancement += 1
Lancement = 0
print("Chargement en cours 80%")
time.sleep(1.5)

while Lancement < 100:
    print("")
    Lancement += 1
Lancement = 0

print("Chargement en cours 100%")
time.sleep(3)

while Lancement < 100:
    print("")
    Lancement += 1

# Debut du jeu 
espace2 = ""
nbEspace2 = 0
b = 0
tourPersonnage = 0
while tourPersonnage < 8:
    tourPersonnage += 1
    if b == 0:
        Espace(0.4, 100)
        print(" O/")
        print("/| <- Sa c'est vous")
        print("/ \ ")

        b = 1

    if b == 1:
        Espace(0.4, 100)
        print(" O__")
        print("/| <- Sa c'est vous")
        print("/ \ ")     
        b = 0

# Gagne cagnotte
Espace(0, 100)
print(" O")
print("/|\ Votre but est d'avoir une bonne vie")
print("/ \ ")

Espace(6, 100)
print(" O")
print("/|\ Votre premiere mission est de gagner de l'argent")
print("/ \ ")

Espace(6, 100)
print(" O")
print("/|\ Pour cela un quizz de question determinera votre capitale de depart")
print("/ \ ")

# Debut du quizz

Espace(6, 100)
print("C'est partit :)")

Espace(2, 100)
AfficheCagnotte()

Espace(3, 100)
reponse = input("1 + 1 = ")
if reponse == "2":
    cagnotte += 2
    print("Juste, Vous gagné 2€")
    Espace(3, 100)
    AfficheCagnotte()
    Espace(3, 100)
else:
    print("Faux, Vous ne gagnez rien")
    Espace(3, 100)
    AfficheCagnotte()
    Espace(3, 100)

Calcule()

