suite = 0
choixOnglet = 0
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
def AfficheCagnotte():
    print("Vous avez " + str(cagnotte) + "€")



def Espace(pause,Inferieur):
    espace2 = ""
    nbEspace2 = 0
    time.sleep(pause)
    while nbEspace2 < Inferieur:
        print("")
        espace2 += " "
        nbEspace2 += 1

def VoitureNul():
    print(Couleur.Vert + "   _______")
    print(               "  / || || \__")
    print(               "   O---------O" + Couleur.Normal)


def VoiturePetite():
    print(Couleur.Vert + "    _____")
    print(               "   /  || \_")
    print(               "   O-------O" + Couleur.Normal)


def Fourgons():
    print("   __________")
    print("o o|_||_||_|_\ ")
    print("    O       O")


def Train():
    print(Couleur.Bleu + " ---    ---- --- -  ____________________")
    print(               "---    - -- -----  |____________________\ ")

def AcheterVoiture():
    suite = 0
    print("Menu",Couleur.Jaune + "Acheter Voiture" + Couleur.Normal)
    print("")
    print("Prix :", Couleur.Jaune + "7.000€" + Couleur.Normal)
    VoitureNul()
    print("Acheter Voiture Nul (n)")
    print("")
    print("Prix :", Couleur.Jaune + "15.000€" + Couleur.Normal)
    VoiturePetite()
    print("Acheter Petite Voiture (l)")
    print("")
    print("Prix :", Couleur.Jaune + "27.000€" + Couleur.Normal)
    Fourgons()
    print("Acheter Fourgons (f)")
    print("")
    print("Prix :", Couleur.Jaune + "160.000€" + Couleur.Normal)
    Train()
    print(Couleur.Normal + "Acheter Train (t)")
    print("")
    print(Couleur.Normal + "Principale (p)")
    try:
        while suite == 0:
            reponse = str(input("Acheter : "))
            if reponse == str(reponse):
                if str(reponse) == "m":
                    if cagnotte >= 7000:
                        choixOnglet = "voiture nul"
                        cagnotte -= 7000
                        Espace(0, 100)
                        print("Vous avez recu (voiture nul)")
                        Espace(2, 100)
                        AfficheCagnotte()
                        Espace(2, 100)
                        choixOnglet = "principale"
                    else:
                        print(Couleur.Rouge + "Vous n'avez pas assez d'argent")
                        Espace(2, 100)
                        choixOnglet = "principale"

AcheterVoiture()
