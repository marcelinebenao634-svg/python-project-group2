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
        print(f"Name        : {self.__name}")
        print(f"Category    : {self.__category}")
        print(f"Description : {self.__description}")
        print(f"Tips        : {self.__tips}")
        print(f"Address     : {self.__address}")
        print(f"Hours       : {self.__hours}")
        print(f"National Price : {self.__national_price} FCFA")
        print(f"Foreign Price  : {self.__foreign_price} FCFA")
        print(f"Rating      : {self.__rating} / 10")

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


class User:
    def __init__(self, last_name, first_name, email, nationality):
        self.__last_name = last_name
        self.__first_name = first_name
        self.__email = email
        self.__nationality = nationality

    def get_last_name(self):
        return self.__last_name
    def get_first_name(self):
        return self.__first_name
    def get_email(self):
        return self.__email
    def get_nationality(self):
        return self.__nationality

    def display_info(self):
        print(f"Name       : {self.__first_name} {self.__last_name}")
        print(f"Email      : {self.__email}")
        print(f"Nationality: {self.__nationality}")


class Reservation:
    reservation_counter = 1

    def __init__(self, user, site, date, nb_persons):
        self.__id = Reservation.reservation_counter
        Reservation.reservation_counter += 1
        self.__user = user
        self.__site = site
        self.__date = date
        self.__nb_persons = nb_persons

        if user.get_nationality().lower() == "burkinabe":
            self.__price_per_person = site.get_national_price()
        else:
            self.__price_per_person = site.get_foreign_price()

        self.__total_price = self.__price_per_person * nb_persons

    def display_reservation(self):
        print("\n========================================")
        print("         RESERVATION CONFIRMATION")
        print("========================================")
        print(f"Reservation ID : #{self.__id}")
        print(f"--- Visitor ---")
        self.__user.display_info()
        print(f"--- Site ---")
        print(f"Site           : {self.__site.get_name()}")
        print(f"Address        : {self.__site.get_address()}")
        print(f"Hours          : {self.__site.get_hours()}")
        print(f"--- Details ---")
        print(f"Date           : {self.__date}")
        print(f"Persons        : {self.__nb_persons}")
        print(f"Price/person   : {self.__price_per_person} FCFA")
        print(f"TOTAL          : {self.__total_price} FCFA")
        print("========================================")


def search_site(site_list, query):
    results = []
    for site in site_list:
        if (query.lower() in site.get_name().lower() or
                query.lower() in site.get_category().lower() or
                query.lower() in site.get_description().lower()):
            results.append(site)
    return results


def register():
    print("\n--- Registration ---")
    last_name = input("Last name : ").strip()
    first_name = input("First name: ").strip()
    email = input("Email     : ").strip()
    nationality = input("Nationality (Burkinabe / Other): ").strip()
    user = User(last_name, first_name, email, nationality)
    print(f"\nWelcome, {first_name} {last_name}! Registration successful.")
    return user


def make_reservation(user, site_list):
    print("\n--- Make a Reservation ---")
    print("Available sites:")
    for i, site in enumerate(site_list):
        print(f"  {i + 1}. {site.get_name()} ({site.get_category()})")

    while True:
        choice = input("\nEnter the site number: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(site_list):
            selected_site = site_list[int(choice) - 1]
            break
        print("Invalid number. Please try again.")

    date = input("Visit date (DD/MM/YYYY): ").strip()

    while True:
        nb = input("Number of persons: ").strip()
        if nb.isdigit() and int(nb) > 0:
            nb_persons = int(nb)
            break
        print("Please enter a valid number.")

    reservation = Reservation(user, selected_site, date, nb_persons)
    reservation.display_reservation()
    return reservation


if __name__ == "__main__":

    site_list = [
        # ── Nature ────────────────────────────────
        TouristSite(
            "Sindou Peaks", "Nature",
            "Majestic rock formations sculpted by erosion over millions of years.",
            "From Banfora, take the road to Sindou (50 km). Walking shoes recommended.",
            "Sindou, Cascades region", "06:00 - 18:00", 500, 2000, 9.9
        ),
        TouristSite(
            "Bala Hippo Pond", "Nature",
            "UNESCO Biosphere Reserve. The largest hippopotamus population in West Africa.",
            "From Bobo-Dioulasso, take the road to Bala. Pirogue available on site.",
            "Bala, near Bobo-Dioulasso", "06:00 - 18:00", 500, 2000, 9.8
        ),
        TouristSite(
            "Karfiguela Waterfall", "Nature",
            "Beautiful natural waterfall surrounded by sugarcane and banana plantations.",
            "12 km from Banfora. Turn left at the green sign. Parking available.",
            "Banfora, Cascades region", "07:00 - 18:00", 500, 2000, 9.6
        ),
        TouristSite(
            "Fabedougou Domes", "Nature",
            "Spectacular geological formations near Banfora. Unique landscape like another planet.",
            "10 km from Banfora. Take the track after the central market.",
            "Fabedougou, near Banfora", "06:00 - 18:00", 500, 2000, 9.5
        ),
        TouristSite(
            "Arli National Park", "Nature",
            "Elephants, buffaloes, lions, crocodiles. WAP complex, East of the country.",
            "70 km from Fada N'Gourma. 4x4 vehicle recommended. Guide mandatory.",
            "East Burkina Faso", "06:00 - 18:00", 500, 2000, 9.6
        ),
        TouristSite(
            "Deux Balés National Park", "Nature",
            "Dense forest sheltering hippos, crocodiles, monkeys and numerous bird species.",
            "From Boromo. Forest tracks require a 4x4. Early morning visits recommended.",
            "Boromo, Boucle du Mouhoun region", "06:00 - 18:00", 500, 2000, 9.2
        ),
        TouristSite(
            "Bantia Botanical Garden", "Nature",
            "Remarkable botanical garden at the gates of Fada N'Gourma.",
            "At the entrance of Fada N'Gourma. Accessible on foot from the city center.",
            "Fada N'Gourma, East region", "08:00 - 17:00", 500, 2000, 9.0
        ),
        TouristSite(
            "Lake Tengrela", "Nature",
            "Tranquil lake near Banfora inhabited by hippos and many water birds.",
            "5 km from Banfora. Pirogue rides available. Ideal at sunrise.",
            "Banfora, Cascades region", "06:00 - 18:00", 500, 1500, 9.4
        ),
        TouristSite(
            "Nazinga Game Ranch", "Nature",
            "Wildlife reserve with one of the densest elephant populations in the Sahel.",
            "From Po, 85 km south. Vehicle and guide mandatory. Accommodation available.",
            "Po, Centre-Sud region", "06:00 - 18:00", 1000, 5000, 9.5
        ),
        TouristSite(
            "Mare aux Hippopotames de Degue-Degue", "Nature",
            "Sacred pond sheltering hippos and crocodiles in a preserved natural setting.",
            "Near Dedougou. Ask locals for directions. Respectful behaviour required.",
            "Dedougou, Boucle du Mouhoun region", "06:00 - 18:00", 500, 1500, 9.1
        ),
        # ── History ───────────────────────────────
        TouristSite(
            "Loropeni Ruins", "History",
            "UNESCO World Heritage 2009. Thousand-year-old stone walls, unique pre-colonial testimony in West Africa.",
            "Take the road to Loropeni from Gaoua. Bring water and a hat.",
            "Loropeni, South-West region", "07:00 - 18:00", 500, 2000, 9.7
        ),
        TouristSite(
            "Tiébélé Royal Court", "History",
            "Traditional Kassena village with extraordinary geometric painted houses, a living architectural heritage.",
            "15 km from Po. Guided visits organized by the village chief's court.",
            "Tiébélé, Centre-Sud region", "08:00 - 17:00", 1000, 3000, 9.8
        ),
        TouristSite(
            "Ruins of Oursi", "History",
            "Ancient fortified village in the Sahel, surrounded by the Oursi pond, a major bird sanctuary.",
            "Near Gorom-Gorom. 4x4 essential. Combine with the Thursday market.",
            "Oursi, Sahel region", "07:00 - 18:00", 500, 1500, 9.1
        ),
        TouristSite(
            "Ruins of Pouni", "History",
            "Vestiges of an ancient Gurunsi settlement with traditional earthen architecture still partially inhabited.",
            "From Sapouy, head towards Pouni. Local guide strongly recommended.",
            "Pouni, Centre-Ouest region", "07:00 - 17:00", 500, 1500, 8.8
        ),
        # ── Culture ───────────────────────────────
        TouristSite(
            "Sacred Crocodiles of Bazoule", "Culture",
            "Thousand-year cohabitation between villagers and hundreds of Nile crocodiles.",
            "30 km from Ouagadougou on the Koudougou road. Guides available on site.",
            "Bazoule, near Ouagadougou", "08:00 - 17:00", 500, 2000, 9.5
        ),
        TouristSite(
            "Laongo Symposium", "Culture",
            "Open-air granite sculptures by artists from around the world.",
            "35 km from Ouagadougou. Take the Ziniare road, follow the signs.",
            "Laongo, 35 km from Ouagadougou", "08:00 - 17:00", 500, 2000, 9.3
        ),
        TouristSite(
            "Gorom-Gorom Market", "Culture",
            "One of the most authentic Sahelian markets in West Africa, held every Thursday.",
            "Travel via Dori from Ouagadougou. Arrive early morning. Bring cash.",
            "Gorom-Gorom, Sahel region", "06:00 - 14:00", 0, 0, 9.6
        ),
        TouristSite(
            "FESPACO - Pan-African Film Festival", "Culture",
            "The largest African cinema festival, held every two years in Ouagadougou since 1969.",
            "Check the biennial schedule (odd years). Book accommodation months in advance.",
            "Ouagadougou, Centre region", "All day during the festival", 2000, 5000, 9.7
        ),
        TouristSite(
            "SIAO - International Crafts Fair", "Culture",
            "Biennial international crafts fair bringing together artisans from all over Africa.",
            "Held in October/November in even years. Located near the airport in Ouagadougou.",
            "Ouagadougou, Centre region", "09:00 - 19:00", 1000, 3000, 9.4
        ),
        TouristSite(
            "Gaoua Poni Museum", "Culture",
            "Regional museum dedicated to the Lobi people, their customs and traditional objects.",
            "In the center of Gaoua. Guided tours recommended to understand Lobi symbolism.",
            "Gaoua, South-West region", "08:00 - 17:00", 500, 1500, 9.0
        ),
        # ── Religion ──────────────────────────────
        TouristSite(
            "Grand Mosque of Bobo-Dioulasso", "Religion",
            "Architectural masterpiece in banco built in 1893. UNESCO listed.",
            "In the center of Bobo-Dioulasso. Accessible on foot from the central market.",
            "Bobo-Dioulasso, Hauts-Bassins region", "08:00 - 17:00", 500, 2000, 9.3
        ),
        TouristSite(
            "Dioulassoba Sacred Grove", "Religion",
            "Ancient animist sacred grove in the heart of the old neighbourhood of Bobo-Dioulasso.",
            "In the Dioulassoba district. Respectful dress required. Guide recommended.",
            "Bobo-Dioulasso, Hauts-Bassins region", "08:00 - 17:00", 500, 1500, 9.1
        ),
        TouristSite(
            "Cathedral of the Immaculate Conception", "Religion",
            "Imposing Catholic cathedral built in 1936, symbol of Ouagadougou's urban landscape.",
            "In the center of Ouagadougou, near the Place de la Nation. Free access.",
            "Ouagadougou, Centre region", "07:00 - 19:00", 0, 0, 8.8
        ),
        TouristSite(
            "Grand Mosque of Ouagadougou", "Religion",
            "One of the largest mosques in West Africa, built in the 1980s, symbol of Islamic architecture in Burkina.",
            "City center of Ouagadougou. Visits outside prayer times. Dress modestly.",
            "Ouagadougou, Centre region", "08:00 - 18:00", 0, 0, 9.0
        ),
        TouristSite(
            "Sacred Forest of Kaya", "Religion",
            "Animist sacred forest used for initiation rites and traditional ceremonies of the Mossi people.",
            "Near Kaya. Access only with a local guide. Photography strictly forbidden.",
            "Kaya, Centre-Nord region", "08:00 - 16:00", 500, 1000, 8.9
        ),
    ]

    current_user = None
    reservations = []

    while True:
        print("\n========================================")
        print("   Tourist Sites of Burkina Faso")
        print("========================================")
        if current_user:
            print(f"   Logged in as: {current_user.get_first_name()} {current_user.get_last_name()}")
        print("========================================")
        print("1. Search for a site")
        print("2. Display all sites")
        print("3. Register / Change user")
        print("4. Make a reservation")
        print("5. View my reservations")
        print("6. Quit")

        choice = input("\nYour choice: ").strip()

        if choice == "1":
            query = input("Enter a name, category or keyword: ").strip()
            if not query:
                print("Please enter a search term.")
                continue
            results = search_site(site_list, query)
            if results:
                print(f"\n{len(results)} site(s) found:")
                for site in results:
                    site.display_info()
            else:
                print("No site found.")

        elif choice == "2":
            print(f"\nAll {len(site_list)} tourist sites:")
            for site in site_list:
                site.display_info()

        elif choice == "3":
            current_user = register()

        elif choice == "4":
            if current_user is None:
                print("Please register first (option 3).")
            else:
                r = make_reservation(current_user, site_list)
                reservations.append(r)

        elif choice == "5":
            if not reservations:
                print("No reservations yet.")
            else:
                print(f"\nYou have {len(reservations)} reservation(s):")
                for r in reservations:
                    r.display_reservation()

        elif choice == "6":
            print("Goodbye! Have a great trip !")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

