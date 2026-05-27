

class Personne:
    def __init__(self, nom, prenom, contact):
        self.__nom = nom
        self.__prenom = prenom
        self.__contact = contact

    def get_nom(self):
        return self.__nom

    def get_prenom(self):
        return self.__prenom

    def get_contact(self):
        return self.__contact

    def afficher(self):
        return f"{self.__prenom} {self.__nom} - {self.__contact}"


class Touriste(Personne):
    def __init__(self, nom, prenom, contact, preferences=None):
        super().__init__(nom, prenom, contact)
        self.__preferences = preferences if preferences is not None else []
        self.__historique = []

    def ajouter_preference(self, preference):
        self.__preferences.append(preference)

    def get_preferences(self):
        return tuple(self.__preferences)

    def ajouter_historique(self, reservation_id):
        self.__historique.append(reservation_id)

    def get_historique(self):
        return list(self.__historique)

    def afficher(self):
        prefs = ", ".join(self.__preferences) if self.__preferences else "Aucune"
        return f"Touriste: {super().afficher()} | Preferences: {prefs}"


class Employe(Personne):
    def __init__(self, nom, prenom, contact, poste, salaire):
        super().__init__(nom, prenom, contact)
        self.__poste = poste
        self.__salaire = salaire

    def get_poste(self):
        return self.__poste

    def get_salaire(self):
        return self.__salaire

    def afficher(self):
        return f"Employe: {super().afficher()} | Poste: {self.__poste} | Salaire: {self.__salaire}"
