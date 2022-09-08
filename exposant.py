# demander 2 nombres avec un exposant chacun puis demander le resultat (differante couleur si juste ou faux)

# changer le texte de couleur

class Couleur:
    Vert= '\033[92m' 
    Bleu = '\033[94m' 
    Rouge = '\033[91m' 
    Normal = '\033[0m' 


n1 = int(input(Couleur.Vert + "Nombre1 sans exposant >> "))
exp1 = int(input("Exposant 1 >> "))

print(Couleur.Bleu, n1 , "exp", exp1)


n2 = int(input(Couleur.Vert + "Nombre2 sans exposant >> "))
exp2 = int(input("Exposant 2 >> "))

print(Couleur.Bleu, n1 , "exp", exp1,"*", n2, "exp", exp2, Couleur.Normal)

if n1 == n2 and exp1 == exp2:
    PCreponseExp = exp1 + exp2
    PCreponseNB = n1
    REPnb = int(input("Resultat Nombre3 sans exposant >> "))  
    REPexp = int(input("Resultat exposant3 >> "))
    
    if REPnb == PCreponseNB:
        print(Couleur.Vert, REPnb)
    else:
        print(Couleur.Rouge + REPnb)

    if REPexp == PCreponseExp:
        print(Couleur.Vert + "Exposant", REPexp)
    else:
        print(Couleur.Rouge + "Exposant", REPexp)    


elif n1 == n2:
    PCreponseExp = exp1 + exp2
    PCreponseNB = n1
    REPnb = int(input("Resultat Nombre3 sans exposant >> "))  
    REPexp = int(input("Resultat exposant3 >> "))
    
    if REPnb == PCreponseNB:
        print(Couleur.Vert, REPnb)
    else:
        print(Couleur.Rouge + REPnb)

    if REPexp == PCreponseExp:
        print(Couleur.Vert + "Exposant", REPexp)
    else:
        print(Couleur.Rouge + "Exposant", REPexp)
# OK

elif exp1 == exp2:
    PCreponseNB1 = n1
    PCreponseNB2 = n2
    PCreponseExp = exp1
    
    REPnb1 = int(input("Resultat Nombre3.1 sans exposant >> "))  
    REPexp1 = int(input("Resultat exposant 3.1 >> "))
    
    
    REPnb2 = int(input("Resultat Nombre3.2 sans exposant >> "))  
    REPexp2 = int(input("Resultat exposant 3.2 >> "))

   
# OK
            
    if REPnb1 == PCreponseNB1:
        Juste1NB = REPnb1
    else:
        Faux1NB = REPnb1

    if REPnb2 == PCreponseNB2:
        Juste2NB = REPnb2
    else:
        Faux2NB = REPnb2
    
    if Juste1NB == REPnb1 and Juste2NB == REPnb2:
        print(Couleur.Vert + "(",Juste1NB,"*",Juste2NB,")")
    
    elif Juste1NB != REPnb1 and Juste2NB == REPnb2:
        print(Couleur.Vert + "(",Couleur.Rouge, Juste1NB," *",Couleur.Vert,Juste2NB,")")

    elif Juste1NB == REPnb1 and Juste2NB != REPnb2:
        print(Couleur.Vert + "(",Juste1NB," *",Couleur.Rouge,Juste2NB,Couleur.Vert + ")") 

    elif Juste1NB != REPnb1 and Juste2NB != REPnb2:
        print(Couleur.Vert + "(",Couleur.Rouge, Juste1NB,Couleur.Vert + "*",Juste2NB,Couleur.Vert + " )")         

   
    if REPexp1 == PCreponseExp:
        print(Couleur.Vert + "Exposant >> ", REPexp1)
    else:
        print(Couleur.Rouge + "Exposant >> ", REPexp1)

