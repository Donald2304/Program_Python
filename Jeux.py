import time,random
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


listeCalcule = list(range(-50 , 50+1))
cagnotte = 0
suite = 0
choixOnglet = "principal"
# Variable competences
Calculator = 0
Mineur = 0
Constructeur = 0
Programmeur = 0


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


def PremiereOrdinateur():
    print("Prix : 150€")
    print("")
    print(Couleur.Gris +"   __|\____      ___")
    print(              "  |  144p  |    |   |")
    print(              " /|________|\   |   |")
    print(              "/___|    |___\  |___|")
    print(              "   _______ ")
    print(              "  |_______| 0 ")

def PuissantOrdinateur():
    print(Couleur.Bleu + " _________")
    print(               "|", Couleur.Violet + "1080p8K", Couleur.Bleu +"|")
    print(               "|_________|" + Couleur.Normal)

    print(Couleur.Rouge + "              _")
    print(Couleur.Vert +  "   ____     ", Couleur.Rouge + "| |")
    print(Couleur.Vert +  "  |____| 0  ", Couleur.Rouge + "|_|")



# Creation fonctions des menus
def MenuPrincipal():
    if choixOnglet == "principale":
        global suite
        Espace(0, 100)
        print("Menu :",Couleur.Jaune +" PRINCIPAL" + Couleur.Normal)
        print("Ordinateur (o)")
        print("Calculs (c)")
        print("Competences (l)")
        while suite == 0:
            try:
                reponse = str(input("Aller dans l'onglet : "))
                if reponse == str(reponse):
                    if str(reponse) == "o":
                        suite = 1
                        choixOnglet = "ordinateur"
                    
                    elif str(reponse) == "c":
                        suite = 1
                        choixOnglet = "calcul"

                    elif str(reponse) == "l":
                        suite = 1
                        choixOnglet = "competence"                    
            except SyntaxError:
                ...

def Calcule():
    if choixOnglet == "calcul":
        gain = 0
        while gain != 300:
            global cagnotte
            nbCalculeOK = 0
            nombre1 = random.choice(listeCalcule)
            nombre2 = random.choice(listeCalcule)
            print(nombre1, "+", nombre2)
            reponseOrdinateur = nombre1 + nombre2
            while nbCalculeOK == 0:
                try:
                    reponse = int(input("Reponse = "))
                    if reponse == int(reponse):
                        nbCalculeOK = 1
                        gain += 50
                except ValueError:
                    ...
            if int(reponse) == reponseOrdinateur:
                print(Couleur.Vert + "Juste, vous gagner 50€." + Couleur.Normal)
                cagnotte += 50
                Espace(3, 100)
                AfficheCagnotte()
                Espace(3, 100)
            elif int(reponse) != reponseOrdinateur:
                print(Couleur.Rouge + "Faux, vous ne gagnez rien." + Couleur.Normal)
                Espace(3, 100)
                AfficheCagnotte()
                Espace(3, 100)


def Competence():   
    if choixOnglet == "competence":    
        print("Menu",Couleur.Jaune + "COMPETENCE" + Couleur.Normal)
        print("Calculer Lvl",Calculator)
        print("Mineur Lvl", Mineur)
        print("Constructeur Lvl", Constructeur)
        print("Programmeur Lvl", Programmeur)


def Ordinateur():
    if choixOnglet == "ordinateur":
        print("Menu", Couleur.Jaune + "Ordinateur")
        print("BTC (b)")
        print("Acheter objet (a)")
        print("Menu principal (p)")
        print("Chercher travail (t)")
        try:
            while suite == 0:
                reponse = str(input("Aller dans l'onglet : "))
                if reponse == str(reponse):
                    if str(reponse) == "b":
                        onglet = "btc"
                        suite = 1

                    elif str(reponse) == "a":
                        onglet = "shopObjet"
                        suite = 1

                    elif str(reponse) == "p":
                        onglet = "principal"
                        suite = 1                    

                    elif str(reponse) == "t":
                        onglet = "chercherTravail"
                        suite = 1
        except SyntaxError:
            ...


def BTC():
    if choixOnglet == "btc":
        print("Menu", Couleur.Jaune + "BTC")
        print("Miner BTC (m)")
        print("Acheter BTC (a)")
        try:
            while suite == 0:
                reponse = str(input("Aller dans l'onglet : "))
                if reponse == (str(reponse)):
                    if str(reponse) == "m":
                        choixOnglet = "miner BTC"
                        suite = 1
                    elif str(reponse) == "a":
                        choixOnglet = "acheter BTC"
                        suite = 1

        except SyntaxError:
            ...
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

# Jeux
nbQuestion = 0
while cagnotte < 300:
    Calcule()
    nbQuestion += 1


# Achat premiere ordinateur

Espace(3, 100)
print("Maintenant que tu as un peu d'argent, allons acheter ton premier ordinateur.")
Espace(6, 100)
PremiereOrdinateur()
print("")
while cagnotte != 150:
    try:
        reponse = str(input(Couleur.Normal + "Appuie sur a pour l'acheter : "))
        if reponse == str(reponse):
            if str(reponse) == "a":
                cagnotte -= 150
                Espace(0, 100)
                print("Tu as recupere (ordinateur ancien)")
                Espace(3, 100)
                AfficheCagnotte()
    except SyntaxError:
        ...

