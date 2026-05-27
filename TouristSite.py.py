class TouristSite:
    def __init__(self, name, category, description, tips, address, hours, national_price, foreign_price, rating):
        self.__name = name
        self.__category = category
        self.__description = description
        self.__tips = tips
        self.__address = address
        self.__hours = hours
        self.__national_price = national_price
        self.__foreign_price = foreign_price
        self.__rating = rating

    def display_info(self):
        print(f"Name: {self.__name}")
        print(f"Category: {self.__category}")
        print(f"Description: {self.__description}")
        print(f"Tips: {self.__tips}")
        print(f"Address: {self.__address}")
        print(f"Hours: {self.__hours}")
        print(f"National Price: {self.__national_price} FCFA")
        print(f"Foreign Price: {self.__foreign_price} FCFA")
        print(f"Rating: {self.__rating} / 10")

    def get_name(self):
        return self.__name
    def get_category(self):
        return self.__category
    def get_description(self):
        return self.__description
    def get_tips(self):
        return self.__tips
    def get_address(self):
        return self.__address
    def get_hours(self):
        return self.__hours
    def get_national_price(self):
        return self.__national_price
    def get_foreign_price(self):
        return self.__foreign_price
    def get_rating(self):
        return self.__rating

def search_site(site_list, name):
    results = []
    for site in site_list:
        if name.lower() in site.get_name().lower() or name.lower() in site.get_category().lower():
            results.append(site)
    return results

site_list = [
    TouristSite(
        "Loropeni Ruins", "History",
        "UNESCO World Heritage 2009. Thousand-year-old stone walls, unique pre-colonial testimony in West Africa.",
        "Take the road to Loropeni from Gaoua. Bring water and a hat.",
        "Loropeni, South-West region", "07:00 - 18:00", 500, 2000, 9.7
    ),
    TouristSite(
        "Bala Hippo Pond", "Nature",
        "UNESCO Biosphere Reserve. The largest hippopotamus population in West Africa.",
        "From Bobo-Dioulasso, take the road to Bala. Pirogue available on site.",
        "Bala, near Bobo-Dioulasso", "06:00 - 18:00", 500, 2000, 9.8
    ),
    TouristSite(
        "Sindou Peaks", "Nature",
        "Majestic rock formations sculpted by erosion over millions of years.",
        "From Banfora, take the road to Sindou (50 km). Walking shoes recommended.",
        "Sindou, Cascades region", "06:00 - 18:00", 500, 2000, 9.9
    ),
    TouristSite(
        "Fabedougou Domes", "Nature",
        "Spectacular geological formations near Banfora. Unique landscape like another planet.",
        "10 km from Banfora. Take the track after the central market.",
        "Fabedougou, near Banfora", "06:00 - 18:00", 500, 2000, 9.5
    ),
    TouristSite(
        "Sacred Crocodiles of Bazoule", "Culture",
        "Thousand-year cohabitation between villagers and hundreds of Nile crocodiles.",
        "30 km from Ouagadougou on the Koudougou road. Guides available on site.",
        "Bazoule, near Ouagadougou", "08:00 - 17:00", 500, 2000, 9.5
    ),
    TouristSite(
        "Karfiguela Waterfall", "Nature",
        "Beautiful natural waterfall surrounded by sugarcane and banana plantations.",
        "12 km from Banfora. Turn left at the green sign. Parking available.",
        "Banfora, Cascades region", "07:00 - 18:00", 500, 2000, 9.6
    ),
    TouristSite(
        "Laongo Symposium", "Culture",
        "Open-air granite sculptures by artists from around the world.",
        "35 km from Ouagadougou. Take the Ziniare road, follow the signs.",
        "Laongo, 35 km from Ouagadougou", "08:00 - 17:00", 500, 2000, 9.3
    ),
    TouristSite(
        "Arli National Park", "Nature",
        "Elephants, buffaloes, lions, crocodiles. WAP complex, East of the country.",
        "70 km from Fada N'Gourma. 4x4 vehicle recommended. Guide mandatory.",
        "East Burkina Faso", "06:00 - 18:00", 500, 2000, 9.6
    ),
    TouristSite(
        "Bantia Botanical Garden", "Nature",
        "Remarkable botanical garden at the gates of Fada N'Gourma.",
        "At the entrance of Fada N'Gourma. Accessible on foot from the city center.",
        "Fada N'Gourma, East region", "08:00 - 17:00", 500, 2000, 9.0
    ),
    TouristSite(
        "Grand Mosque of Bobo-Dioulasso", "Religion",
        "Architectural masterpiece in banco built in 1893. UNESCO listed.",
        "In the center of Bobo-Dioulasso. Accessible on foot from the central market.",
        "Bobo-Dioulasso, Hauts-Bassins region", "08:00 - 17:00", 500, 2000, 9.3
    )
]

while True:
    print("\n=== Tourist Sites of Burkina Faso ===")
    print("1. Search for a site")
    print("2. Display all sites")
    print("3. Quit")

    choice = input("Your choice: ")

    if choice == "1":
        name = input("Enter the name of the site to search: ")
        results = search_site(site_list, name)
        if results:
            for site in results:
                site.display_info()
        else:
            print("No site found.")

    elif choice == "2":
        for site in site_list:
            site.display_info()

    elif choice == "3":
        print("Goodbye!")
