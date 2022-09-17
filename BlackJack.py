# faire le jeu du blackjack
import random
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
    Gris = '\033[90m'
    RougeClair = '\033[91m'
    VertClair = '\033[92m'
    Jaune = '\033[93m'
    Rose = '\033[95m'
    CyanClair = '\033[96m'


cagnotte = 10
print("Cagnotte :", cagnotte)

while True:
    try:
        ChoixCagnotte = int(input("Choix mises : "))
        while ChoixCagnotte > 10 or ChoixCagnotte < 1:
            if ChoixCagnotte > cagnotte:
                print('Mises trop élevé')
                ChoixCagnotte = int(input("Choix mises : "))
            elif ChoixCagnotte < 1:
                print("Mise trop petite")
                ChoixCagnotte = int(input("Choix mises : "))
        break
    except ValueError:
        print("Ce n'est pas un nombre")



cagnotte -= ChoixCagnotte
listeCarte = [2, 2 , 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11]
a = True
TotalCroupier = 0
totj = 0
b = 1
t1 = '?'
t2 = '?'
t3 = '?'
t4 = '?'
t5 = '?'
t6 = '?'
t7 = '?'
t8 = '?'
t9 = '?'
t10 = '?'

c1 = '?'
c2 = '?'
c3 = '?'
c4 = '?'
c5 = '?'
c6 = '?'
c7 = '?'
c8 = '?'
c9 = '?'
c10 = '?'


tour = 0

CarteJoueur = random.choice(listeCarte)
listeCarte.remove(CarteJoueur)



totj += CarteJoueur

def Croupier():
    global TotalCroupier
    global cagnotte
    global b
    if TotalCroupier > 21 and b == 1:
        print('Joueur Gagne')
        cagnotte += 2 * ChoixCagnotte
        print("Cagnotte Joueur :",cagnotte)
        b = 0
    elif TotalCroupier == 21 and b == 1:
        print("Croupier Gagne")
        cagnotte == 2 * ChoixCagnotte
        print("Cagnotte Joueur :",cagnotte)
        b = 0
    if totj < 21:
        if TotalCroupier < 17:
            time.sleep(2)
            CarteCroupier = random.choice(listeCarte)
            listeCarte.remove(CarteCroupier)
            print(Couleur.Normal + 'Carte Croupier :',CarteCroupier)
            TotalCroupier += CarteCroupier
            print(Couleur.Rouge + 'Total Croupier :',TotalCroupier,Couleur.Normal)


Perdant = []
Gagnant = []



def tableau():
    global t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, totj
    if tour == 1:
        t1 = random.choice(listeCarte)
        totj = t1
        listeCarte.remove(CarteJoueur) 
    elif tour == 2:
        t2 = random.choice(listeCarte)
        totj = t1 + t2
        listeCarte.remove(CarteJoueur) 
    elif tour == 3:
        t3 = random.choice(listeCarte)
        totj = t1 + t2 + t3
        listeCarte.remove(CarteJoueur) 
    elif tour == 4:
        t4 = random.choice(listeCarte)
        totj = t1 + t2 + t3 + t4
        listeCarte.remove(CarteJoueur) 
    elif tour == 5:
        t5 = random.choice(listeCarte)
        totj = t1 + t2 + t3 + t4 + t5
        listeCarte.remove(CarteJoueur) 
    elif tour == 6:
        t6 = random.choice(listeCarte)
        totj = t1 + t2 + t3 + t4 + t5 + t6
        listeCarte.remove(CarteJoueur) 
    elif tour == 7:
        t7 = random.choice(listeCarte)
        totj = t1 + t2 + t3 + t4 + t5 + t6 + t7
        listeCarte.remove(CarteJoueur) 
    elif tour == 8:
        t8 = random.choice(listeCarte)
        totj = t1 + t2 + t3 + t4 + t5 + t6 + t7 + t8
        listeCarte.remove(CarteJoueur) 
    elif tour == 9:
        t9 = random.choice(listeCarte)
        totj = t1 + t2 + t3 + t4 + t5 + t6 + t7 + t8 + t9
        listeCarte.remove(CarteJoueur) 
    elif tour == 10:
        t10 = random.choice(listeCarte)
        totj = t1 + t2 + t3 + t4 + t5 + t6 + t7 + t8 + t9 + t10
        listeCarte.remove(CarteJoueur) 
    print("        |Carte1||Carte2||Carte3||Carte4||Carte5||Carte6||Carte7||Carte8||Carte9||Carte10||Total|")
    print("JOUEUR  |",t1.rjust(6),"||",t2.rjust(6),"||",t3.rjust(6),"||",t4.rjust(6),"||",t5.rjust(6),"||",t6.rjust(6),"||",t7.rjust(6),"||",t8.rjust(6),"||",t9.rjust(6),"||",t10.rjust(7),"||",totj.rjust(5),"|")
    print("CROUPIER|      ||      ||      ||      ||      ||      ||      ||      ||      ||       ||     |")
    if tour == 1:
        t1 = CarteJoueur
    if tour == 2:
        t2 = CarteJoueur
    if tour == 3:
        t3 = CarteJoueur
    if tour == 4:
        t4 = CarteJoueur
    if tour == 5:
        t5 = CarteJoueur
    if tour == 6:
        t6 = CarteJoueur
    if tour == 7:
        t7 = CarteJoueur
    if tour == 8:
        t8 = CarteJoueur
    if tour == 9:
        t9 = CarteJoueur
    if tour == 10:
        t10 = CarteJoueur





def Joueur():
    global totj
    global cagnotte
    global b
    if totj > 21 and b == 1:
        time.sleep(2)
        print('Croupier Gagne')
        cagnotte -= ChoixCagnotte
        print("Cagnotte Joueur :",cagnotte)
        b = 0

    
    elif totj == 21 and b == 1:
        time.sleep(2)
        print("Joueur Gagne")
        cagnotte += 2 * ChoixCagnotte
        print("Cagnotte Joueur :",cagnotte)
        b = 0


    if totj < 21:
        if TotalCroupier < 21:
            print('')
            time.sleep(2)
            Choix = input("Distribuer ou rester : ")
            if Choix == 'd':
                tableau()
                print('Carte Joueur :',CarteJoueur)
            elif Choix == 'r':
                global a
                a = False
                while TotalCroupier < 17:
                    Croupier()
                if TotalCroupier < 22 and totj < 22 and TotalCroupier == totj:
                    print("Egalite")
                    print("Cagnotte Joueur :",cagnotte)
                elif TotalCroupier > totj and TotalCroupier < 22:
                    print('Gagnant : Croupier')
                    cagnotte -= ChoixCagnotte
                    print("Cagnotte Joueur :",cagnotte)
                elif TotalCroupier < totj and totj < 22:
                    print('Gagnant : Joueur')
                    cagnotte += 2 * ChoixCagnotte
                    print("Cagnotte Joueur :",cagnotte)

while a:
    tour += 1
    if tour == 1:
        t1 = CarteJoueur
    elif  tour == 2:
        t2 = CarteJoueur
    elif tour == 3:
        t3 = CarteJoueur
    elif tour == 4:
        t4 = CarteJoueur
    elif tour == 5:
        t5 = CarteJoueur
    elif tour == 6:
        t6 = CarteJoueur
    elif tour == 7:
        t7 = CarteJoueur
    elif tour == 8:
        t8 = CarteJoueur
    elif tour == 9:
        t9 = CarteJoueur
    elif tour == 10:
        t10 = CarteJoueur
    tableau()
    Croupier()
    Joueur()

Perdant = []
Gagnant = []



