# Pour changer la couleur du texte
class Couleur:
    Vert= '\033[92m' 
    Bleu = '\033[94m' 
    Rouge = '\033[91m' 
    Normal = '\033[0m' 

print(Couleur.Bleu + " |___||___|")
print(               "x|___||___|")
print(               " ----------" + Couleur.Normal)

print("")


colonne1H = int(input("Chiffre dizaine H >> "))

print(Couleur.Bleu + " |",colonne1H,"||___|")
print(               "x|___||___|")
print(               " ----------" + Couleur.Normal)


colonne2H = int(input("Chiffre Unité H >> "))

print("")

print(Couleur.Bleu + " |",colonne1H,"||",colonne2H,"|")
print(              "x|___||___|")
print(               " ----------" + Couleur.Normal)


colonne1B = int(input("Chiffre Dizaine B >> "))

print("")

print(Couleur.Bleu + " |",colonne1H,"||",colonne2H,"|")
print(              "x|",colonne1B,"||___|")
print(               " ----------" + Couleur.Normal)


colonne2B = int(input("Chiffre Unité B >> "))

print("")

print(Couleur.Bleu + " |",colonne1H,"||",colonne2H,"|")
print(              "x|",colonne1B,"||",colonne2B,"|")
print(               " ----------" + Couleur.Normal)


print("")

print(Couleur.Bleu +"          |",colonne1H,"||",colonne2H,"|")
print(              "         x|",colonne1B,"||",colonne2B,"|")
print(               "----------------------" + Couleur.Normal)
print(Couleur.Bleu + "     |___||___||___|")
print(Couleur.Bleu + "|___||___||___|| 0 |" + Couleur.Normal)

ReponseC31 = colonne2B * colonne2H

if ReponseC31 > 9:
    x = [int(a) for a in str(ReponseC31)]
    a = x[0]
    b =  x[1]
    ReponseC31 = b    

print("")
print("")
print("")

UReponse31 = int(input("Ligne 1.3 >> "))

RefaireAdditions = []
AdditionErreur = 0

if UReponse31 == ReponseC31:
    print(Couleur.Bleu +"          |",colonne1H,"||",colonne2H,"|")
    print(              "         x|",colonne1B,"||",colonne2B,"|")
    print(               "----------------------" + Couleur.Normal)
    print(Couleur.Bleu + "     |___||___||",UReponse31,"|")
    print(Couleur.Bleu + "|___||___||___|| 0 |")


elif UReponse31 != ReponseC31:
    RefaireAdditions.append(UReponse31)
    AdditionErreur += 1
    print(Couleur.Bleu +"          |",colonne1H,"||",colonne2H,"|")
    print(              "         x|",colonne1B,"||",colonne2B,"|")
    print(               "----------------------" + Couleur.Normal)
    print(Couleur.Rouge + "     |___||___|| X |")
    print(Couleur.Bleu + "|___||___||___|| 0 |")

ReponseC21 = colonne2B * colonne1H

if ReponseC21 > 9:
    x = [int(a) for a in str(ReponseC21)]
    a = x[0]
    b =  x[1]
    ReponseC21 = b    
    ReponseC21 += a

print("")
print("")
print("")

UReponse21 = int(input("Ligne 1.2 >> "))

if UReponse21 == ReponseC21 and AdditionErreur == 0:
    print(Couleur.Bleu +"          |",colonne1H,"||",colonne2H,"|")
    print(              "         x|",colonne1B,"||",colonne2B,"|")
    print(               "----------------------" + Couleur.Normal)
    print(Couleur.Bleu + "     |___||",UReponse21,"||",UReponse31,"|")
    print(Couleur.Bleu + "|___||___||___|| 0 |")


elif UReponse21 == ReponseC21 and AdditionErreur != 0:    
    print(Couleur.Bleu +"          |",colonne1H,"||",colonne2H,"|")
    print(              "         x|",colonne1B,"||",colonne2B,"|")
    print(               "----------------------" + Couleur.Normal)
    print(Couleur.Rouge + "     |___||",UReponse21,"|| X |")
    print(Couleur.Bleu + "|___||___||___|| 0 |")


elif UReponse21 != ReponseC21 and AdditionErreur == 0:
    RefaireAdditions.append(UReponse21)
    print(Couleur.Bleu +"          |",colonne1H,"||",colonne2H,"|")
    print(              "         x|",colonne1B,"||",colonne2B,"|")
    print(               "----------------------" + Couleur.Normal)
    print(Couleur.Rouge + "     |___|| X ||",UReponse31,"|")
    print(Couleur.Bleu + "|___||___||___|| 0 |")

elif UReponse21 != ReponseC21 and AdditionErreur != 0:
    RefaireAdditions.append(UReponse21)
    print(Couleur.Bleu +"          |",colonne1H,"||",colonne2H,"|")
    print(              "         x|",colonne1B,"||",colonne2B,"|")
    print(               "----------------------" + Couleur.Normal)
    print(Couleur.Rouge + "     |___|| X || X |")
    print(Couleur.Bleu + "|___||___||___|| 0 |")



ReponseC11 = colonne2B * colonne2B

if ReponseC11 > 9:
    x = [int(a) for a in str(ReponseC11)]
    a = x[0]
    b =  x[1]
    ReponseC11 = b    

ReponseC11 += a-1


print("")
print("")
print("")

UReponse11 = int(input("Ligne 1.1 >> "))


if UReponse11 == ReponseC11 and  UReponse21 == ReponseC21 and UReponse31 == ReponseC31:         # tout juste
    print(Couleur.Bleu +"          |",colonne1H,"||",colonne2H,"|")
    print(              "         x|",colonne1B,"||",colonne2B,"|")
    print(               "----------------------" + Couleur.Normal)
    print(Couleur.Bleu + "     |",UReponse11,"||",UReponse21,"||",UReponse31,"|")
    print(Couleur.Bleu + "|___||___||___|| 0 |")


elif UReponse11 == ReponseC11 and UReponse21 == ReponseC21 and UReponse31 != ReponseC31:    # erreur colonne 1
    print(Couleur.Bleu +"          |",colonne1H,"||",colonne2H,"|")
    print(              "         x|",colonne1B,"||",colonne2B,"|")
    print(               "----------------------" + Couleur.Normal)
    print(Couleur.Rouge + "     |",UReponse11,"||",UReponse21,"|| X |")
    print(Couleur.Bleu + "|___||___||___|| 0 |")


elif UReponse11 == ReponseC11 and UReponse21 != ReponseC21 and UReponse31 == ReponseC31: # erreur colonne 2
    RefaireAdditions.append(UReponse21)
    print(Couleur.Bleu +"          |",colonne1H,"||",colonne2H,"|")
    print(              "         x|",colonne1B,"||",colonne2B,"|")
    print(               "----------------------" + Couleur.Normal)
    print(Couleur.Rouge + "     |",UReponse11,"|| X ||",UReponse31,"|")
    print(Couleur.Bleu + "|___||___||___|| 0 |")

elif UReponse11 != ReponseC11 and  UReponse21 == ReponseC21 and UReponse31 == ReponseC31:         # erreur colonne 3
    print(Couleur.Bleu +"          |",colonne1H,"||",colonne2H,"|")
    print(              "         x|",colonne1B,"||",colonne2B,"|")
    print(               "----------------------" + Couleur.Normal)
    print(Couleur.Rouge + "     | X ||",UReponse21,"||",UReponse31,"|")
    print(Couleur.Bleu + "|___||___||___|| 0 |")


elif UReponse11 == ReponseC11 and UReponse21 != ReponseC21 and UReponse31 != ReponseC31:      # erreur colonnes 1 et 2
    RefaireAdditions.append(UReponse21)
    print(Couleur.Bleu +"          |",colonne1H,"||",colonne2H,"|")
    print(              "         x|",colonne1B,"||",colonne2B,"|")  
    print(               "----------------------" + Couleur.Normal)
    print(Couleur.Rouge + "     |",UReponse11,"|| X || X |")
    print(Couleur.Bleu + "|___||___||___|| 0 |")

elif UReponse11 != ReponseC11 and  UReponse21 == ReponseC21 and UReponse31 != ReponseC31:         # erreur colonne 1 et 3
    print(Couleur.Bleu +"          |",colonne1H,"||",colonne2H,"|")
    print(              "         x|",colonne1B,"||",colonne2B,"|")
    print(               "----------------------" + Couleur.Normal)
    print(Couleur.Rouge + "     | X ||",UReponse21,"|| X |")
    print(Couleur.Bleu + "|___||___||___|| 0 |")

elif UReponse11 != ReponseC11 and  UReponse21 != ReponseC21 and UReponse31 == ReponseC31:         # erreur colonne 2 et 3
    print(Couleur.Bleu +"          |",colonne1H,"||",colonne2H,"|")
    print(              "         x|",colonne1B,"||",colonne2B,"|")
    print(               "----------------------" + Couleur.Normal)
    print(Couleur.Rouge + "     | X || X ||",UReponse31,"|")
    print(Couleur.Bleu + "|___||___||___|| 0 |")

elif UReponse11 != ReponseC11 and  UReponse21 != ReponseC21 and UReponse31 != ReponseC31:         # erreur colonne 1 et 2 et 3
    print(Couleur.Bleu +"          |",colonne1H,"||",colonne2H,"|")
    print(              "         x|",colonne1B,"||",colonne2B,"|")
    print(               "----------------------" + Couleur.Normal)
    print(Couleur.Rouge + "     | X || X || X |")
    print(Couleur.Bleu + "|___||___||___|| 0 |")
# OK

ReponseC23 = colonne1B * colonne2H 
UReponse23 = int(input("Colonne 2.3 >> ")) 

if UReponse23 == ReponseC23 and  UReponse11 == ReponseC11 and  UReponse21 == ReponseC21 and UReponse31 == ReponseC31:         # tout juste
    print(Couleur.Bleu +"          |",colonne1H,"||",colonne2H,"|")
    print(              "         x|",colonne1B,"||",colonne2B,"|")
    print(               "----------------------" + Couleur.Normal)
    print(Couleur.Bleu + "     |",UReponse11,"||",UReponse21,"||",UReponse31,"|")
    print(Couleur.Bleu + "|___||___||",UReponse23,"|| 0 |")



if UReponse23 == ReponseC23 and  UReponse11 == ReponseC11 and  UReponse21 == ReponseC21 and UReponse31 != ReponseC31:         # erreur colonne 1H
    print(Couleur.Bleu +"          |",colonne1H,"||",colonne2H,"|")
    print(              "         x|",colonne1B,"||",colonne2B,"|")
    print(               "----------------------" + Couleur.Normal)
    print(Couleur.Rouge + "     |",UReponse11,"||",UReponse21,"|| X |")
    print(Couleur.Bleu + "|___||___||",UReponse23,"|| 0 |")



if UReponse23 == ReponseC23 and  UReponse11 == ReponseC11 and  UReponse21 != ReponseC21 and UReponse31 == ReponseC31:         # erreur colonne 2H
    print(Couleur.Bleu +"          |",colonne1H,"||",colonne2H,"|")
    print(              "         x|",colonne1B,"||",colonne2B,"|")
    print(               "----------------------" + Couleur.Normal)
    print(Couleur.Rouge + "     |",UReponse11,"|| X ||",UReponse31,"|")
    print(Couleur.Bleu + "|___||___||",UReponse23,"|| 0 |")



if UReponse23 == ReponseC23 and  UReponse11 != ReponseC11 and  UReponse21 == ReponseC21 and UReponse31 == ReponseC31:         # erreur colonne 3H
    print(Couleur.Bleu +"          |",colonne1H,"||",colonne2H,"|")
    print(              "         x|",colonne1B,"||",colonne2B,"|")
    print(               "----------------------" + Couleur.Normal)
    print(Couleur.Rouge + "     | X ||",UReponse21,"||",UReponse31,"|")
    print(Couleur.Bleu + "|___||___||",UReponse23,"|| 0 |")


if UReponse23 == ReponseC23 and  UReponse11 == ReponseC11 and  UReponse21 != ReponseC21 and UReponse31 != ReponseC31:         # erreur colonne 1H et 2H
    print(Couleur.Bleu +"          |",colonne1H,"||",colonne2H,"|")
    print(              "         x|",colonne1B,"||",colonne2B,"|")
    print(               "----------------------" + Couleur.Normal)
    print(Couleur.Rouge + "     |",UReponse11,"|| X || X |")
    print(Couleur.Bleu + "|___||___||",UReponse23,"|| 0 |")


if UReponse23 == ReponseC23 and  UReponse11 == ReponseC11 and  UReponse21 == ReponseC21 and UReponse31 == ReponseC31:         # erreur colonne 1H et 3H
    print(Couleur.Bleu +"          |",colonne1H,"||",colonne2H,"|")
    print(              "         x|",colonne1B,"||",colonne2B,"|")
    print(               "----------------------" + Couleur.Normal)
    print(Couleur.Rouge + "     | X ||",UReponse21,"|| X |")
    print(Couleur.Bleu + "|___||___||",UReponse23,"|| 0 |")


if UReponse23 == ReponseC23 and  UReponse11 != ReponseC11 and  UReponse21 != ReponseC21 and UReponse31 == ReponseC31:         # erreur colonne 2 et 3
    print(Couleur.Bleu +"          |",colonne1H,"||",colonne2H,"|")
    print(              "         x|",colonne1B,"||",colonne2B,"|")
    print(               "----------------------" + Couleur.Normal)
    print(Couleur.Rouge + "     | X || X ||",UReponse31,"|")
    print(Couleur.Bleu + "|___||___||",UReponse23,"|| 0 |")


if UReponse23 == ReponseC23 and  UReponse11 != ReponseC11 and  UReponse21 != ReponseC21 and UReponse31 != ReponseC31:         # erreur 1H et 2H et 3H
    print(Couleur.Bleu +"          |",colonne1H,"||",colonne2H,"|")
    print(              "         x|",colonne1B,"||",colonne2B,"|")
    print(               "----------------------" + Couleur.Normal)
    print(Couleur.Rouge + "     | X || X || X |")
    print(Couleur.Bleu + "|___||___||",UReponse23,"|| 0 |")


if UReponse23 != ReponseC23 and  UReponse11 != ReponseC11 and  UReponse21 != ReponseC21 and UReponse31 != ReponseC31:         # Erreur 1H et 2H et 3H et 1B
    print(Couleur.Bleu +"          |",colonne1H,"||",colonne2H,"|")
    print(              "         x|",colonne1B,"||",colonne2B,"|")
    print(               "----------------------" + Couleur.Normal)
    print(Couleur.Rouge + "     | X || X || X |")
    print(Couleur.Rouge + "|___||___|| X || 0 |")



if UReponse23 != ReponseC23 and  UReponse11 == ReponseC11 and  UReponse21 == ReponseC21 and UReponse31 != ReponseC31:         # Erreur 1H et 1B
    print(Couleur.Bleu +"          |",colonne1H,"||",colonne2H,"|")
    print(              "         x|",colonne1B,"||",colonne2B,"|")
    print(               "----------------------" + Couleur.Normal)
    print(Couleur.Rouge + "     |",UReponse11,"||",UReponse21,"|| X |")
    print(Couleur.Rouge + "|___||___|| X || 0 |")


if UReponse23 != ReponseC23 and  UReponse11 == ReponseC11 and  UReponse21 != ReponseC21 and UReponse31 == ReponseC31:         # Erreur colonne 2H et 1B
    print(Couleur.Bleu +"          |",colonne1H,"||",colonne2H,"|")
    print(              "         x|",colonne1B,"||",colonne2B,"|")
    print(               "----------------------" + Couleur.Normal)
    print(Couleur.Rouge + "     |",UReponse11,"|| X ||",UReponse31,"|")
    print(Couleur.Rouge + "|___||___|| X || 0 |")


if UReponse23 != ReponseC23 and  UReponse11 != ReponseC11 and  UReponse21 == ReponseC21 and UReponse31 == ReponseC31:         # 3H et 1B
    print(Couleur.Bleu +"          |",colonne1H,"||",colonne2H,"|")
    print(              "         x|",colonne1B,"||",colonne2B,"|")
    print(               "----------------------" + Couleur.Normal)
    print(Couleur.Rouge + "     | X ||",UReponse21,"||",UReponse31,"|")
    print(Couleur.Rouge + "|___||___|| X || 0 |")


if UReponse23 != ReponseC23 and  UReponse11 == ReponseC11 and  UReponse21 != ReponseC21 and UReponse31 != ReponseC31:         # 1H et 2H et 1B
    print(Couleur.Bleu +"          |",colonne1H,"||",colonne2H,"|")
    print(              "         x|",colonne1B,"||",colonne2B,"|")
    print(               "----------------------" + Couleur.Normal)
    print(Couleur.Rouge + "     |",UReponse11,"|| X || X |")
    print(Couleur.Rouge + "|___||___||",UReponse23,"|| 0 |")


if UReponse23 != ReponseC23 and  UReponse11 != ReponseC11 and  UReponse21 == ReponseC21 and UReponse31 != ReponseC31:         # 1H et 3H et 1B
    print(Couleur.Bleu +"          |",colonne1H,"||",colonne2H,"|")
    print(              "         x|",colonne1B,"||",colonne2B,"|")
    print(               "----------------------" + Couleur.Normal)
    print(Couleur.Rouge + "     | X  ||",UReponse21,"|| X |")
    print(Couleur.Rouge + "|___||___|| X || 0 |")



if UReponse23 != ReponseC23 and  UReponse11 != ReponseC11 and  UReponse21 != ReponseC21 and UReponse31 == ReponseC31:         # 2H et 3H et 1B
    print(Couleur.Bleu +"          |",colonne1H,"||",colonne2H,"|")
    print(              "         x|",colonne1B,"||",colonne2B,"|")
    print(               "----------------------" + Couleur.Normal)
    print(Couleur.Rouge + "     | X || X ||",UReponse31,"|")
    print(Couleur.Rouge + "|___||___|| X || 0 |")


if UReponse23 != ReponseC23 and  UReponse11 != ReponseC11 and  UReponse21 != ReponseC21 and UReponse31 != ReponseC31:         # 1H et 2H et 3H et 1B
    print(Couleur.Bleu +"          |",colonne1H,"||",colonne2H,"|")
    print(              "         x|",colonne1B,"||",colonne2B,"|")
    print(               "----------------------" + Couleur.Normal)
    print(Couleur.Bleu + "     | X || X || X |")
    print(Couleur.Bleu + "|___||___|| X || 0 |")


















