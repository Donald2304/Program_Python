# plus d'option pour le code sur les exposants

#Permet de changer les couleurs du texte 
class Couleur:
    Vert= '\033[92m' 
    Bleu = '\033[94m' 
    Rouge = '\033[91m' 
    Normal = '\033[0m'
    Violet = '\033[95m'
    Blanc = '\033[97m' 


# afficher les options de calculs
print(Couleur.Vert + "OPTIONS 1 : a^n * a^m")
print("OPTIONS 2 : (a^n)^m")
print("OPTIONS 3 : 1/a^n")
print("OPTIONS 4 : a^n/a^m")
print("OPTIONS 5 : a^0")
print("OPTIONS 6 : (AB)^n ")


# demander l'option a choisir
print('')
ChoixCalcul = int(input("Choisir options : "+ Couleur.Bleu))


# verifier le choix de calcul
if ChoixCalcul > 6 or ChoixCalcul < 1:
    Erreur = 1
    print(Couleur.Rouge + "Cette options n'existe pas :/")
else:
    Erreur = 0
    print(Couleur.Vert + "L'options",ChoixCalcul,"a était choisit")

  
# lancer les questions ou quitter en appuyant sur une touche
if Erreur == 0:
    StartProgram = str(input(Couleur.Vert + "(c)->continuer | (q)->quitter : " + Couleur.Bleu))
    

    # Verifie si les bonnes touches ont étaient pressé
    if StartProgram == "q":
        print(Couleur.Rouge + "Fin du programme :/")
        Erreur = 1    
    
    elif StartProgram == "c":
        print('')
        print(Couleur.Vert + "Lancement du programme ... :)")
        Continuer = 1

    elif StartProgram != "c" or StartProgram != "q":
        print(Couleur.Rouge + "Choix Indisponible :/")
        Erreur = 1                  


# Si la touche (c) a était pressé 
if Erreur == 0 and Continuer == 1:
    
    # Pose les questions sur les nombres et les exposants

    # Option 1 
    if ChoixCalcul == 1:
        
        # Pose les questions
        Nombre_1 = int(input(Couleur.Vert + "Nombre sans exposant : " + Couleur.Bleu))
        Exposant_1 = int(input(Couleur.Vert + "Premier Exposant : " + Couleur.Bleu))
        Exposant_2 = int(input(Couleur.Vert + "Deuxieme Exposant : " + Couleur.Bleu))
        
        print('')
        print('')
        
        print(Couleur.Blanc,Nombre_1,"^",Exposant_1,"*",Nombre_1,"^",Exposant_2)
        
        print('')
        print('')

        print(Couleur.Vert + "Donner une reponse sous le format | a^n+m : " + Couleur.Bleu)
        ReponseNB = int(input("Reponse pour (a) : " + Couleur.Bleu))
        ReponseExposant = int(input("Reponse pour (^n+m) : " + Couleur.Bleu))
        
        # Calcul Ordinateur
        a = Nombre_1
        NM = Exposant_1 + Exposant_2

        # Verifie les reponses
        if a == ReponseNB:
            print(Couleur.Vert + "Nombre_",ReponseNB)
        else:
            print(Couleur.Rouge + "Nombre_",ReponseNB)
        if NM == ReponseExposant:
            print(Couleur.Vert + "Exposant_",ReponseExposant)
        else:
            print(Couleur.Rouge + "Exposant_",ReponseExposant)
        

    # Option 2
    if ChoixCalcul == 2:

        Nombre_1 = int(input(Couleur.Vert + "Nombre sans exposant : " + Couleur.Bleu))
        Exposant_1 = int(input(Couleur.Vert + "Premier Exposant : " + Couleur.Bleu))
        Exposant_2 = int(input(Couleur.Vert + "Deuxieme Exposant : " + Couleur.Bleu))
        
        print('')
        print('')
        
        print(Couleur.Blanc + "(",Nombre_1,"^",Exposant_1,")","^",Exposant_2)
        
        print('')
        print('')

        print(Couleur.Vert + "Donner une reponse sous le format | (a^n)^m : " + Couleur.Bleu)
        ReponseNB = int(input("Reponse pour (a) : " + Couleur.Bleu))
        ReponseExposant = int(input("Reponse pour (^n*m) : " + Couleur.Bleu))
        
        # Calcul Ordinateur
        a = Nombre_1
        NM = Exposant_1 * Exposant_2

        # Verifie les reponses
        if a == ReponseNB:
            print(Couleur.Vert + "Nombre_",ReponseNB)
        else:
            print(Couleur.Rouge + "Nombre_",ReponseNB)
        if NM == ReponseExposant:
            print(Couleur.Vert + "Exposant_",ReponseExposant)
        else:
            print(Couleur.Rouge + "Exposant_",ReponseExposant)
    

    # Options 3 
    if ChoixCalcul == 3:
        Nombre = int(input("Nombre sans exposant : "))
        Exposant = int(input("Exposant : "))

        print('')
        print('')
        
        print(Couleur.Blanc + "1 /",Nombre,"^",Exposant)

        print('')
        print('')

        print(Couleur.Vert + "Donner une reponse sous le format | 1/a^n : " + Couleur.Bleu)
        ReponseNB = int(input("Reponse pour (a) : " + Couleur.Bleu))
        ReponseExposant = int(input("Reponse pour (^n) : " + Couleur.Bleu))

        # Calcule Ordinateur
        a = Nombre
        RepExp = -Exposant

        # Verifie les reponses
        if a == ReponseNB:
            print(Couleur.Vert + "Nombre_",ReponseNB)
        else:
            print(Couleur.Rouge + "Nombre_",ReponseNB)
        if RepExp == ReponseExposant:
            print(Couleur.Vert + "Exposant_",ReponseExposant)
        else:
            print(Couleur.Rouge + "Exposant_",ReponseExposant)

    # Option 4
    if ChoixCalcul == 4:
        Nombre = int(input("Nombre sans exposant : "))
        Exposant_1 = int(input("Exposant 1 : "))
        Exposant_2 = int(input("Exposant 2 : "))

        print('')
        print('')

        print(Couleur.Blanc, Nombre,"^",Exposant_1,"/",Nombre,"^",Exposant_2)

        print('')
        print('')

        print(Couleur.Vert + "Donner une reponse sous le format (a^n/a^m) : " + Couleur.Bleu)
        ReponseNB = int(input("Reponse pour (a) : " + Couleur.Bleu))
        ReponseExposant1 = int(input("Reponse pour (^n) : " + Couleur.Bleu))
        ReponseExposant2 = int(input("Reponse pour (^m) : " + Couleur.Bleu))

        # Calcule Ordinateur
        a = Nombre
        RepExp1 = Exposant_1
        RepExp2 = -Exposant_2

        # Verifie les reponses
        if a == ReponseNB:
            print(Couleur.Vert + "Nombre_",ReponseNB)
        else:
            print(Couleur.Rouge + "Nombre",ReponseNB)
            
        if RepExp1 == ReponseExposant1:
            print(Couleur.Vert + "Exposant_",ReponseExposant1)
        else:
            print(Couleur.Rouge + "Exposant_",ReponseExposant1)

        print('')

        if RepExp2 == ReponseExposant2:
            print(Couleur.Vert + "Nombre_",a)
            print(Couleur.Vert + "Exposant_",ReponseExposant2)
        else:
            print(Couleur.Vert + "Nombre_ ",a)
            print(Couleur.Rouge + "Exposant_",ReponseExposant2)
        
        print('')

        RepExposant3 = RepExp1 + RepExp2
        ReponseMoins = int(input("Simplifier l'exposant : "))
        print('')
        if ReponseMoins == RepExposant3:
            print(Couleur.Vert + "Nombre",Nombre)
            print(Couleur.Vert + "Exposant simplifier",ReponseMoins)
        else:
            print(Couleur.Vert + "Nombre Simplifier",Nombre)
            print(Couleur.Rouge,ReponseMoins)


    # Option 5
        
    if ChoixCalcul == 5:
        Nombre = int(input(Couleur.Vert + "Nombre sans exposant : "))
        print("Que donne", Nombre,"^ 0")
        Reponse = int(input("Reponse : "))
        if Reponse == 1:
            print(Couleur.Vert,Nombre,"^ 0 = 1")
        else:
            print(Couleur.Rouge,Nombre,"^ 0 =",Reponse)

    # Option 6
    if ChoixCalcul == 6:
        Nombre_1 = int(input("Nombre 1 sans exposant : "))
        Nombre_2 = int(input("Nombre 2 sans exposant : "))
        Exposant = int(input("Exposant : "))

        print('')
        print('')


        ReponseNombre1 = int(input("Nombre 1 : "))
        ExposantNombre1 = int(input("Exposant nombre 1 : "))
        ReponseNombre2 = int(input("Nombre 2 : "))
        ExposantNombre2 = int(input("Exposant nombre 2 : ")) 

        print('')
        print('')

        if ReponseNombre1 == Nombre_1:
            print(Couleur.Vert,"Nombre1 : ",ReponseNombre1)
        else:
            print(Couleur.Rouge,"Nombre1 : ",ReponseNombre1)
        
        if ExposantNombre1 == Exposant:
            print(Couleur.Vert,"Exposant1 : ",Exposant)
        else:
            print(Couleur.Rouge,"Exposant1 : ",Exposant)

        print('')
        
        if ReponseNombre2 == Nombre_2:
            print(Couleur.Vert,"Nombre2 : ", ReponseNombre2)
        else:
            print(Couleur.Rouge,"Nombre2 : ", ReponseNombre2)

        if ExposantNombre2 == Exposant:
            print(Couleur.Vert,"Exposant2 : ",Exposant)
        else:
            print(Couleur.Rouge,"Exposant2 : ",Exposant)

        print('')

        print("Maintenant presentez sous cette forme (ab)^n")
        ReponseA = int(input(Couleur.Vert + "(a) est a l'exposant : "))
        ReponseB = int(input(Couleur.Vert + "(b) est a l'exposant : "))
        
        print('')

        if ReponseA == Exposant:
            print(Couleur.Vert + "Nombre1 : ",Nombre_1)
            print("Exposant1 : ",ReponseA)
        else:
            print(Couleur.Vert + "Nombre1 : ",Nombre_1)
            print(Couleur.Rouge + "Exposant1 : ",ReponseB)

        if ReponseB == Exposant:
            print(Couleur.Vert + "Nombre2 : ",Nombre_2)
            print("Exposant2 : ",ReponseA)
        else:
            print(Couleur.Vert + "Nombre2 : ",Nombre_2)
            print(Couleur.Rouge + "Exposant2 : ",ReponseB)






