class UnHumain:
    def __init__(self, c_prenom, c_age):
        print("Création d'un Humain...")
        self.prenom = c_prenom
        self.age = c_age



print("Lancement du programme...")

h1 = UnHumain("Jojo", 34)
print("Prenom de h1 : {}".format(h1.prenom))
print("Age de h1 : {}".format(h1.age))

h2 = UnHumain("Albert", 17)
print("Prenom de h2 : {}".format(h2.prenom))
print("Age de h2 : {}".format(h2.age))
