import time

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

Debut = 0
espace = ""
nbEspace = 0
a = 0
barre = "-"
nbBarre = 0

while Debut == 0:
    try:
        Lanceur = str(input("Lancer le jeu(j) = "))
        if Lanceur == "j":
            Debut = 1
    except SyntaxWarning:
        ...

while Debut == 0:
    while a < 25:
        print('')
        a +=1
    if nbEspace > 205:
        espace = ""
        nbEspace = 0
    if nbBarre > 205:
        barre =  "-"
        nbBarre = 0
    espace += " "
    barre += "-"
    nbBarre += 1
    nbEspace += 1
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    time.sleep(0.1)
    print(Couleur.Jaune + "       ____")
    print(                "      |    |")
    print(                "      |____|"+ Couleur.Normal)
    print(Couleur.Gris+" _______ ___ _____   __          __ ___ _ ________ __ _ __________ ______ ____ _ _ ___ __ _ _ _ __ _ __ __   ___________      ________ __    ___ _ __ _ __ _ __ _____ _ _______________")
    print("_______ __________      _______    ____     _ _ _______ __ ____ _          ________ _ _ _ ______ _ ________ __ __ __ ___           ___ _  _ _ ____ ___ __ __ ______ __ ___ _________ __" + Couleur.Normal)


    print("")
    print("")
    print("")
    print("")
    print("")
    print(espace + Couleur.Rouge +" _________")
    print(espace +               "  / || || \ ")
    print(espace +               "   O---------O" + Couleur.Normal)
    print("--------------------------"+barre) 
     
