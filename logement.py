"""
logement.py - Accommodation base class and subclasses (Hotel, Auberge).
Demonstrates polymorphism via calculate_price().
"""

class Accommodation:
    """Base class for tourist accommodations."""
    def __init__(self, name, location, base_price):
        self.__name = name
        self.__location = location
        self.__base_price = base_price

    def get_name(self): return self.__name
    def get_location(self): return self.__location
    def get_base_price(self): return self.__base_price

    def calculate_price(self, nights):
        return self.__base_price * nights

    def display(self):
        print(f"  {self.__name} | {self.__location} | {self.__base_price} FCFA/night")


class Hotel(Accommodation):
    """Hotel with star rating and services. Applies 5% tax."""
    def __init__(self, name, location, base_price, stars, services):
        super().__init__(name, location, base_price)
        self.__stars = stars
        self.__services = services

    def get_stars(self): return self.__stars
    def get_services(self): return self.__services

    def calculate_price(self, nights):
        return super().calculate_price(nights) * 1.05

    def display(self):
        price = self.calculate_price(1)
        print(f"  Hotel: {self.get_name()} ({self.__stars} stars) | {self.get_location()} | {price:.0f} FCFA/night | Services: {', '.join(self.__services)}")


class Auberge(Accommodation):
    """Auberge with dormitory type. Applies 10% discount."""
    def __init__(self, name, location, base_price, dorm_type):
        super().__init__(name, location, base_price)
        self.__dorm_type = dorm_type

    def get_dorm_type(self): return self.__dorm_type

    def calculate_price(self, nights):
        return super().calculate_price(nights) * 0.90

    def display(self):
        price = self.calculate_price(1)
        print(f"  Auberge: {self.get_name()} | {self.get_location()} | {price:.0f} FCFA/night | Dorm: {self.__dorm_type}")


# Accommodation Database mapped to regions
ACCOMMODATION_DB = [
    Hotel("Memorial Hotel", "Ouagadougou", 45000, 4, ["Wi-Fi", "Pool", "Restaurant"]),
    Hotel("Bravia Hotel", "Ouagadougou", 40000, 4, ["Wi-Fi", "Conference Rooms"]),
    Auberge("Auberge Song Taaba", "Ouagadougou", 20000, "Mixed Dorm"),
    Hotel("Hotel Sissiman", "Bobo-Dioulasso", 35000, 4, ["Wi-Fi", "Pool", "Gym"]),
    Hotel("Villa Bobo", "Bobo-Dioulasso", 30000, 3, ["Wi-Fi", "Breakfast"]),
    Auberge("Auberge Bilimpo", "Bobo-Dioulasso", 18000, "Female Dorm"),
    Hotel("Cascades Palace", "Banfora", 35000, 4, ["Wi-Fi", "Pool", "Restaurant"]),
    Hotel("Hotel Calypso", "Banfora", 30000, 3, ["Wi-Fi", "AC Bungalows"]),
    Auberge("Auberge de la Falaise", "Banfora", 15000, "Mixed Dorm"),
    Hotel("Splendide Hotel", "Koudougou", 30000, 4, ["Wi-Fi", "Pool"]),
    Auberge("Auberge Plateau Central", "Koudougou", 15000, "Female Dorm"),
    Hotel("Hotel Dunia", "Ouahigouya", 25000, 3, ["Wi-Fi", "Restaurant"]),
    Auberge("Auberge du Nord", "Ouahigouya", 18000, "Mixed Dorm"),
    Hotel("Hotel Kazienide", "Kaya", 25000, 3, ["Wi-Fi", "24h Reception"]),
    Hotel("Pacific Hotel Kaya", "Kaya", 30000, 3, ["Wi-Fi", "Restaurant"]),
    Auberge("Auberge du Centre", "Kaya", 12000, "Male Dorm"),
    Hotel("Zind Naaba Hotel", "Dedougou", 25000, 4, ["Wi-Fi", "Pool"]),
    Auberge("Campement Touristique", "Dedougou", 15000, "Mixed Dorm"),
    Hotel("Panache Hotel", "Fada N'Gourma", 28000, 3, ["Wi-Fi", "Hot Water", "AC"]),
    Auberge("Auberge du 11 Decembre", "Fada N'Gourma", 18000, "Mixed Dorm"),
    Hotel("Eco-Touristic Oasis", "Tenkodogo", 25000, 4, ["Wi-Fi", "Private Bath"]),
    Auberge("Auberge Poko et Raogo", "Tenkodogo", 15000, "Female Dorm"),
    Hotel("Gaoua Lodge", "Gaoua", 22000, 3, ["Wi-Fi", "Breakfast"]),
    Auberge("Auberge du Sud", "Gaoua", 14000, "Mixed Dorm")
]
