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

    def display(self):
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

    def calculate_price(self):
        return self.get_cost() * 1.05

    def display(self):
        print("Hotel Information:")
        super().display()
        print(f"Stars: {self.__stars} stars")
        print(f"Services: {', '.join(self.__services)}")
        print(f"cost with taxe 5%: {self.calculate_price()} FCFA")


class Auberge(Logement):
    """Auberge class with type of dormitory. 10% discount applied."""

    def __init__(self, name, localisation, cost, type_dormitory):
        super().__init__(name, localisation, cost)
        self.__type_dormitory = type_dormitory

    def get_type_dormitory(self):
        return self.__type_dormitory

    def calculate_price(self):
        return self.get_cost() * 0.90

    def display(self):
        print("\nAuberge Information:")
        super().display()
        print(f"Type of Dormitory: {self.__type_dormitory}")
        print(f"cost with discount 10%: {self.calculate_price()}FCFA")
    
