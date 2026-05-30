"""
TouristSite.py - Site management, categorization, and security filtering.
Contains the full database of 25 Burkina Faso sites.
"""

class TouristSite:
    """Represents a tourist destination with detailed information."""
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
        
        # AUTOMATIC LOGIC FOR COMPATIBILITY WITH main.py
        # Extracts the city/region from the address for accommodation filtering
        self.__region = self._extract_region(address)
        # Determines the security level based on the region
        self.__security = self._assign_security(self.__region)

    def _extract_region(self, address):
        """Extracts the key city from the address to filter accommodations."""
        address_lower = address.lower()
        if "banfora" in address_lower: return "Banfora"
        if "bobo" in address_lower: return "Bobo-Dioulasso"
        if "ouaga" in address_lower: return "Ouagadougou"
        if "gaoua" in address_lower: return "Gaoua"
        if "kaya" in address_lower: return "Kaya"
        if "fada" in address_lower: return "Fada N'Gourma"
        if "dedougou" in address_lower: return "Dedougou"
        if "po" in address_lower: return "Po"
        if "gorom" in address_lower: return "Gorom-Gorom"
        # Fallback: takes the first word before the comma
        return address.split(",")[0].strip()

    def _assign_security(self, region):
        """Assigns a default security level based on the region."""
        high_sec = ["Ouagadougou", "Bobo-Dioulasso", "Banfora", "Koudougou"]
        medium_sec = ["Gaoua", "Dedougou", "Kaya", "Tenkodogo"]
        if region in high_sec: return "High"
        if region in medium_sec: return "Medium"
        return "Low"  # Remote or border areas

    # ───────── GETTERS ─────────
    def get_name(self): return self.__name
    def get_category(self): return self.__category
    def get_description(self): return self.__description
    def get_tips(self): return self.__tips
    def get_address(self): return self.__address
    def get_hours(self): return self.__hours
    def get_national_price(self): return self.__national_price
    def get_foreign_price(self): return self.__foreign_price
    def get_rating(self): return self.__rating
    # Getters required by main.py for filtering
    def get_region(self): return self.__region
    def get_security(self): return self.__security
    def get_price(self): return self.__national_price

    def display_info(self):
        print(f"  Name: {self.__name}")
        print(f"  Category: {self.__category}")
        print(f"  Description: {self.__description}")
        print(f"  Tips: {self.__tips}")
        print(f"  Address: {self.__address}")
        print(f"  Hours: {self.__hours}")
        print(f"  National Price: {self.__national_price} FCFA")
        print(f"  Foreign Price: {self.__foreign_price} FCFA")
        print(f"  Rating: {self.__rating} / 10\n")


# ───────── COMPLETE DATABASE (25 SITES) ─────────
SITE_DATABASE = [
    # ── Nature ────────────────────────────────
    # 1.
    TouristSite(
        "Sindou Peaks", "Nature",
        "Majestic rock formations sculpted by erosion over millions of years.",
        "From Banfora, take the road to Sindou (50 km). Walking shoes recommended.",
        "Sindou, Cascades region", "06:00 - 18:00", 500, 2000, 9.9
    ),
    # 2.
    TouristSite(
        "Bala Hippo Pond", "Nature",
        "UNESCO Biosphere Reserve. The largest hippopotamus population in West Africa.",
        "From Bobo-Dioulasso, take the road to Bala. Pirogue available on site.",
        "Bala, near Bobo-Dioulasso", "06:00 - 18:00", 500, 2000, 9.8
    ),
    # 3.
    TouristSite(
        "Karfiguela Waterfall", "Nature",
        "Beautiful natural waterfall surrounded by sugarcane and banana plantations.",
        "12 km from Banfora. Turn left at the green sign. Parking available.",
        "Banfora, Cascades region", "07:00 - 18:00", 500, 2000, 9.6
    ),
    # 4.
    TouristSite(
        "Fabedougou Domes", "Nature",
        "Spectacular geological formations near Banfora. Unique landscape like another planet.",
        "10 km from Banfora. Take the track after the central market.",
        "Fabedougou, near Banfora", "06:00 - 18:00", 500, 2000, 9.5
    ),
    # 5.
    TouristSite(
        "Arli National Park", "Nature",
        "Elephants, buffaloes, lions, crocodiles. WAP complex, East of the country.",
        "70 km from Fada N'Gourma. 4x4 vehicle recommended. Guide mandatory.",
        "East Burkina Faso", "06:00 - 18:00", 500, 2000, 9.6
    ),
    # 6.
    TouristSite(
        "Deux Balés National Park", "Nature",
        "Dense forest sheltering hippos, crocodiles, monkeys and numerous bird species.",
        "From Boromo. Forest tracks require a 4x4. Early morning visits recommended.",
        "Boromo, Boucle du Mouhoun region", "06:00 - 18:00", 500, 2000, 9.2
    ),
    # 7.
    TouristSite(
        "Bantia Botanical Garden", "Nature",
        "Remarkable botanical garden at the gates of Fada N'Gourma.",
        "At the entrance of Fada N'Gourma. Accessible on foot from the city center.",
        "Fada N'Gourma, East region", "08:00 - 17:00", 500, 2000, 9.0
    ),
    # 8.
    TouristSite(
        "Lake Tengrela", "Nature",
        "Tranquil lake near Banfora inhabited by hippos and many water birds.",
        "5 km from Banfora. Pirogue rides available. Ideal at sunrise.",
        "Banfora, Cascades region", "06:00 - 18:00", 500, 1500, 9.4
    ),
    # 9.
    TouristSite(
        "Nazinga Game Ranch", "Nature",
        "Wildlife reserve with one of the densest elephant populations in the Sahel.",
        "From Po, 85 km south. Vehicle and guide mandatory. Accommodation available.",
        "Po, Centre-Sud region", "06:00 - 18:00", 1000, 5000, 9.5
    ),
    # 10.
    TouristSite(
        "Mare aux Hippopotames de Degue-Degue", "Nature",
        "Sacred pond sheltering hippos and crocodiles in a preserved natural setting.",
        "Near Dedougou. Ask locals for directions. Respectful behaviour required.",
        "Dedougou, Boucle du Mouhoun region", "06:00 - 18:00", 500, 1500, 9.1
    ),

    # ── History ───────────────────────────────
    # 11.
    TouristSite(
        "Loropeni Ruins", "History",
        "UNESCO World Heritage 2009. Thousand-year-old stone walls, unique pre-colonial testimony in West Africa.",
        "Take the road to Loropeni from Gaoua. Bring water and a hat.",
        "Loropeni, South-West region", "07:00 - 18:00", 500, 2000, 9.7
    ),
    # 12.
    TouristSite(
        "Tiébélé Royal Court", "History",
        "Traditional Kassena village with extraordinary geometric painted houses, a living architectural heritage.",
        "15 km from Po. Guided visits organized by the village chief's court.",
        "Tiébélé, Centre-Sud region", "08:00 - 17:00", 1000, 3000, 9.8
    ),
    # 13.
    TouristSite(
        "Ruins of Oursi", "History",
        "Ancient fortified village in the Sahel, surrounded by the Oursi pond, a major bird sanctuary.",
        "Near Gorom-Gorom. 4x4 essential. Combine with the Thursday market.",
        "Oursi, Sahel region", "07:00 - 18:00", 500, 1500, 9.1
    ),
    # 14.
    TouristSite(
        "Ruins of Pouni", "History",
        "Vestiges of an ancient Gurunsi settlement with traditional earthen architecture still partially inhabited.",
        "From Sapouy, head towards Pouni. Local guide strongly recommended.",
        "Pouni, Centre-Ouest region", "07:00 - 17:00", 500, 1500, 8.8
    ),

    # ── Culture ───────────────────────────────
    # 15.
    TouristSite(
        "Sacred Crocodiles of Bazoule", "Culture",
        "Thousand-year cohabitation between villagers and hundreds of Nile crocodiles.",
        "30 km from Ouagadougou on the Koudougou road. Guides available on site.",
        "Bazoule, near Ouagadougou", "08:00 - 17:00", 500, 2000, 9.5
    ),
    # 16.
    TouristSite(
        "Laongo Symposium", "Culture",
        "Open-air granite sculptures by artists from around the world.",
        "35 km from Ouagadougou. Take the Ziniare road, follow the signs.",
        "Laongo, 35 km from Ouagadougou", "08:00 - 17:00", 500, 2000, 9.3
    ),
    # 17.
    TouristSite(
        "Gorom-Gorom Market", "Culture",
        "One of the most authentic Sahelian markets in West Africa, held every Thursday.",
        "Travel via Dori from Ouagadougou. Arrive early morning. Bring cash.",
        "Gorom-Gorom, Sahel region", "06:00 - 14:00", 0, 0, 9.6
    ),
    # 18.
    TouristSite(
        "FESPACO - Pan-African Film Festival", "Culture",
        "The largest African cinema festival, held every two years in Ouagadougou since 1969.",
        "Check the biennial schedule (odd years). Book accommodation months in advance.",
        "Ouagadougou, Centre region", "All day during the festival", 2000, 5000, 9.7
    ),
    # 19.
    TouristSite(
        "SIAO - International Crafts Fair", "Culture",
        "Biennial international crafts fair bringing together artisans from all over Africa.",
        "Held in October/November in even years. Located near the airport in Ouagadougou.",
        "Ouagadougou, Centre region", "09:00 - 19:00", 1000, 3000, 9.4
    ),
    # 20.
    TouristSite(
        "Gaoua Poni Museum", "Culture",
        "Regional museum dedicated to the Lobi people, their customs and traditional objects.",
        "In the center of Gaoua. Guided tours recommended to understand Lobi symbolism.",
        "Gaoua, South-West region", "08:00 - 17:00", 500, 1500, 9.0
    ),

    # ── Religion ──────────────────────────────
    # 21.
    TouristSite(
        "Grand Mosque of Bobo-Dioulasso", "Religion",
        "Architectural masterpiece in banco built in 1893. UNESCO listed.",
        "In the center of Bobo-Dioulasso. Accessible on foot from the central market.",
        "Bobo-Dioulasso, Hauts-Bassins region", "08:00 - 17:00", 500, 2000, 9.3
    ),
    # 22.
    TouristSite(
        "Dioulassoba Sacred Grove", "Religion",
        "Ancient animist sacred grove in the heart of the old neighbourhood of Bobo-Dioulasso.",
        "In the Dioulassoba district. Respectful dress required. Guide recommended.",
        "Bobo-Dioulasso, Hauts-Bassins region", "08:00 - 17:00", 500, 1500, 9.1
    ),
    # 23.
    TouristSite(
        "Cathedral of the Immaculate Conception", "Religion",
        "Imposing Catholic cathedral built in 1936, symbol of Ouagadougou's urban landscape.",
        "In the center of Ouagadougou, near the Place de la Nation. Free access.",
        "Ouagadougou, Centre region", "07:00 - 19:00", 0, 0, 8.8
    ),
    # 24.
    TouristSite(
        "Grand Mosque of Ouagadougou", "Religion",
        "One of the largest mosques in West Africa, built in the 1980s, symbol of Islamic architecture in Burkina.",
        "City center of Ouagadougou. Visits outside prayer times. Dress modestly.",
        "Ouagadougou, Centre region", "08:00 - 18:00", 0, 0, 9.0
    ),
    # 25.
    TouristSite(
        "Sacred Forest of Kaya", "Religion",
        "Animist sacred forest used for initiation rites and traditional ceremonies of the Mossi people.",
        "Near Kaya. Access only with a local guide. Photography strictly forbidden.",
        "Kaya, Centre-Nord region", "08:00 - 16:00", 500, 1000, 8.9
    )
]


def display_sites_by_category():
    """Groups sites by category and displays them with numbered IDs."""
    categories = {}
    for site in SITE_DATABASE:
        categories.setdefault(site.get_category(), []).append(site)

    print("\n--- Available Tourist Sites (Grouped by Category & Security) ---")
    idx = 1
    site_map = {}
    for cat in sorted(categories.keys()):
        print(f"\n[Category: {cat}]")
        for site in categories[cat]:
            print(f"  {idx}. {site.get_name()} (Security: {site.get_security()})")
            print(f"     Region: {site.get_region()} | Price: {site.get_price()} FCFA")
            site_map[idx] = site
            idx += 1
    return site_map


if __name__ == "__main__":
    # Quick test: display the list
    display_sites_by_category()