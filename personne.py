

class Personne:
    def __init__(self, nom, prenom, contact):
        # Attributs privés : on ne les modifie pas directement de l'extérieur.
        self.__nom = nom
        self.__prenom = prenom
        self.__contact = contact

