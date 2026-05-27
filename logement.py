class Logement:
    """Base class representing a tourist accomodation."""

    def __init__(self, name, localisation, cost):
        self.__name = name
        self.__localisation = localisation
        self.__cost = cost

    def get_name(self):
        return self.__name

    def get_localisation(self):
        return self.__localisation

    def get_cost(self):
        return self.__cost

    def afficher(self):
        print(f"Logement: {self.__name}")
        print(f"Localisation: {self.__localisation}")
        print(f"Cost: {self.__cost} FCFA")


class Hotel(Logement):
    """Hotel class with stars and services. 5% tax applied."""

    def __init__(self, name, localisation, cost, stars, services):
        super().__init__(name, localisation, cost)
        self.__stars = stars
        self.__services = services

    def get_stars(self):
        return self.__stars

    def calculer_prix(self):
        return self.get_cost() * 1.05

    def afficher(self):
        print("Hotel Information:")
        super().afficher()
        print(f"Stars: {self.__stars} stars")
        print(f"Services: {', '.join(self.__services)}")
        print(f"cost with taxe 5%: {self.calculer_prix()} FCFA")


class Auberge(Logement):
    """Auberge class with type of dormitory. 10% discount applied."""

    def __init__(self, name, localisation, cost, type_dormitory):
        super().__init__(name, localisation, cost)
        self.__type_dormitory = type_dormitory

    def get_type_dormitory(self):
        return self.__type_dormitory

    def calculer_prix(self):
        return self.get_cost() * 0.90

    def afficher(self):
        print("\nAuberge Information:")
        super().afficher()
        print(f"Type of Dormitory: {self.__type_dormitory}")
        print(f"cost with discount 10%: {self.calculer_prix()} FCFA")


if __name__ == "__main__":
    hotel1 = Hotel("Hotel Splendide", "OUAGADOUGOU", 50000, 4, ["Wi-Fi", "Piscine"])
    auberge1 = Auberge("Auberge Bilimpo", "Fada N'Gourma", 20000, "Mixed Dormitory")
    hotel2 = Hotel("Hotel de la Paix", "Lagos", 30000, 3, ["Wi-Fi", "Restaurant"])
    auberge2 = Auberge("Auberge du 11 Decembre", "Fada N'Gourma", 15000, "Female Dormitory")
    hotel3 = Hotel("Laico hotel", "OUAGADOUGOU", 40000, 5, ["Wi-Fi", "Piscine", "Spa"])
    auberge3 = Auberge("Auberge song taaba", "OUAGADOUGOU", 25000, "Male Dormitory")
    hotel4 = Hotel("Hotel silmende", "OUAGADOUGOU", 35000, 4, ["Wi-Fi", "Piscine", "Restaurant"])
    auberge4 = Auberge("Auberge du LA VIDA LOCA", "OUAGADOUGOU", 18000, "Female Dormitory")
    hotel5 = Hotel("Bravia Hotel", "OUAGADOUGOU", 45000, 5, ["Wi-Fi", "Piscine", "Spa", "Restaurant"])
    hotel6 = Hotel("Lancaster ouaga 2000", "OUAGADOUGOU", 55000, 5, ["Wi-Fi", "Piscine", "Spa", "Restaurant"])
    hotel7 = Hotel("Hotel kavana", "OUAGADOUGOU", 40000, 4, ["Wi-Fi", "Piscine"])
    hotel8 = Hotel("Bravia Hotel", "OUAGADOUGOU", 45000, 5, ["Wi-Fi", "Piscine", "Spa", "Restaurant"])
    hotel9 = Hotel("hotel sissiman", "Bobo-Dioulasso", 35000, 4, ["Wi-Fi", "Piscine", "Restaurant"])
    hotel10 = Hotel("villa Bobo", "Bobo-Dioulasso", 30000, 3, ["Wi-Fi", "Piscine"])
    hotel11 = Hotel("pacific hotel", "Bobo-Dioulasso", 40000, 4, ["Wi-Fi", "Piscine", "Restaurant"])
    hotel12 = Hotel("cascades Palace", "Banfora", 45000, 3, ["Wi-Fi", "Piscine", "Spa", "Restaurant"])
    hotel13 = Hotel("Hotel canne a sucre", "Banfora ", 30000, 3, ["Wi-Fi", "Piscine"])
    hotel14 = Hotel("Hotel du lac", "Banfora", 35000, 4, ["Wi-Fi", "Piscine", "Restaurant"])
    hotel15 = Hotel("campement touristique", "Dedougou", 25000, 2, ["Wi-Fi"])
    hotel16 = Hotel("Hotel Tieba", "Tenkodogo", 20000, 2, ["Wi-Fi"])
    hotel17 = Hotel("Hotel djamou", "Tenkodogo", 30000, 3, ["Wi-Fi", "Piscine"])
    hotel18 = Hotel("Hotel du kaziende", "Kaya", 35000, 4, ["Wi-Fi", "Piscine", "Restaurant"])
    hotel19 = Hotel("pacific hotel kaya", "Kaya", 40000, 4, ["Wi-Fi", "Piscine", "Restaurant"])
    hotel20 = Hotel("Hotel la grace divine", "Kaya", 45000, 5, ["Wi-Fi", "Piscine", "Spa", "Restaurant"])
    hotel1.afficher()
    print("\n")
    auberge1.afficher()
    print("\n")
    hotel2.afficher()
    print("\n")
    auberge2.afficher()
    print("\n")
    hotel3.afficher()
    print("\n")
    auberge3.afficher()
    print("\n")
    hotel4.afficher()
    print("\n")
    auberge4.afficher()
    print("\n")
    hotel5.afficher()
    print("\n")
    hotel6.afficher()
    print("\n")
    hotel7.afficher()
    print("\n")
    hotel8.afficher()
    print("\n")
    hotel9.afficher()
    print("\n")
    hotel10.afficher()
    print("\n")
    hotel11.afficher()
    print("\n")
    hotel12.afficher()
    print("\n")
    hotel13.afficher()
    print("\n")
    hotel14.afficher()
    print("\n")
    hotel15.afficher()
    print("\n")
    hotel16.afficher()
    print("\n")
    hotel17.afficher()
    print("\n")
    hotel18.afficher()
    print("\n")
    hotel19.afficher()
    print("\n")
    hotel20.afficher()
