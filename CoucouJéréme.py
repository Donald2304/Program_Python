import time
a = 0 
espace = ""
nbEspace = 0
while True:
    if a == 0:
        espace = ""
        nbEspace = 0
        time.sleep(0.4)
        while nbEspace < 100:
            print("")
            espace += " "        
            nbEspace += 1
        print(" O/")
        print("/|")
        print("/ \ ")

        a = 1

    if a == 1:
        espace = ""
        nbEspace = 0
        time.sleep(0.4)
        while nbEspace < 100:
            print("")
            espace += " "
            nbEspace += 1
        print(" O__")
        print("/|")
        print("/ \ ")     
        a = 0
