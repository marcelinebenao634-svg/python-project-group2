"""
main.py - Entry point for the AfriTour system.
Handles user routing, site selection, accommodation booking, and receipt generation.
"""
from personne import Tourist, Employee
from logement import Hotel, Auberge, ACCOMMODATION_DB
from TouristSite import SITE_DATABASE
from reservation import Reservation

VALID_PAYMENTS = ("Cash", "Credit Card", "Mobile Money", "Bank Transfer")


def get_valid_input(prompt, validator=lambda x: True, error_msg="Invalid input."):
    while True:
        val = input(prompt).strip()
        if validator(val):
            return val
        print(error_msg)


def filter_accommodations_by_region(region):
    return [acc for acc in ACCOMMODATION_DB if acc.get_location().lower() == region.lower()]


def employee_dashboard(user):
    print("\nEmployee Dashboard")
    print(f"Welcome, Agent {user.get_first_name()} {user.get_last_name()}")
    print(f"Position: {user.get_position()} | Contact: {user.get_contact()}")
    print("=" * 50)
    while True:
        print("\nManagement Menu:")
        print("1. View all sites & security levels")
        print("2. View all accommodations")
        print("3. System statistics")
        print("4. Update site security")
        print("5. Update accommodation price")
        print("6. Search sites")
        print("7. Quit")
        choice = get_valid_input("Your choice: ", lambda x: x in "1234567")
        
        if choice == "1":
            for i, s in enumerate(SITE_DATABASE, 1):
                print(f"  {i}. {s.get_name()} | {s.get_region()} | {s.get_security()}")
        elif choice == "2":
            for i, a in enumerate(ACCOMMODATION_DB, 1):
                print(f"  {i}. {a.get_name()} | {a.get_location()} | {a.get_base_price()} FCFA")
        elif choice == "3":
            print(f"\nTotal Sites: {len(SITE_DATABASE)}")
            print(f"Total Accommodations: {len(ACCOMMODATION_DB)}")
        elif choice == "4":
            idx = int(get_valid_input("Site number: ", lambda x: x.isdigit()))
            if 1 <= idx <= len(SITE_DATABASE):
                new_sec = get_valid_input("New level (High/Medium/Low): ", lambda x: x.title() in ["High","Medium","Low"])
                SITE_DATABASE[idx-1].__dict__["_TouristSite__security"] = new_sec.title()
                print("Updated.")
        elif choice == "5":
            idx = int(get_valid_input("Accommodation number: ", lambda x: x.isdigit()))
            if 1 <= idx <= len(ACCOMMODATION_DB):
                new_price = int(get_valid_input("New price (FCFA): ", lambda x: x.isdigit()))
                ACCOMMODATION_DB[idx-1].__dict__["_Accommodation__base_price"] = new_price
                print("Updated.")
        elif choice == "6":
            q = get_valid_input("Keyword: ", lambda x: len(x)>0)
            res = [s for s in SITE_DATABASE if q.lower() in s.get_name().lower() or q.lower() in s.get_description().lower()]
            print(f"\nFound {len(res)} site(s):")
            for s in res: print(f"  - {s.get_name()} ({s.get_category()})")
        elif choice == "7":
            print("\nGoodbye . Thanks for update")
            break


def main():
    print("Welcome to AfriTour System\n")

    # 1. Coordinates & Role
    last = get_valid_input("Last name: ", lambda x: len(x)>0, "Required.")
    first = get_valid_input("First name: ", lambda x: len(x)>0, "Required.")
    contact = get_valid_input("Phone/Email: ", lambda x: len(x)>=5, "Enter valid contact.")
    role = get_valid_input("Role (Tourist/Employee): ", lambda x: x.lower() in ["tourist","employee"], "Type Tourist or Employee.")

    if role.lower() == "tourist":
        user = Tourist(last, first, contact)
        print("\nTravel Preferences (type 'done' to finish):")
        while True:
            p = input("Add preference (e.g., Nature, History, Culture, Safari): ").strip()
            if p.lower() == "done" or p == "":
                break
            user.add_preference(p)
    else:
        user = Employee(last, first, contact, "Agent", 0)
        employee_dashboard(user)
        return

    print(f"\nProfile: {user.display()}\n")

    # 2. Choose Sites (Affinity-based display)
    prefs = user.get_preferences()
    site_map = {}
    idx = 1

    print("\n--- Available Tourist Sites ---")

    if prefs:
        matching = [s for s in SITE_DATABASE if any(p.lower() in s.get_category().lower() or p.lower() in s.get_name().lower() for p in prefs)]
        others = [s for s in SITE_DATABASE if s not in matching]

        if matching:
            print(f"\n[ Recommended based on your preferences: {', '.join(prefs)} ]")
            for s in matching:
                print(f"  {idx}. {s.get_name()} (Security: {s.get_security()})")
                print(f"     Region: {s.get_region()} | Price: {s.get_price()} FCFA")
                site_map[idx] = s
                idx += 1

        if others:
            print("\n[ Other Available Sites ]")
            for s in others:
                print(f"  {idx}. {s.get_name()} (Security: {s.get_security()})")
                print(f"     Region: {s.get_region()} | Price: {s.get_price()} FCFA")
                site_map[idx] = s
                idx += 1
    else:
        print("\n[ All Sites ]")
        for s in SITE_DATABASE:
            print(f"  {idx}. {s.get_name()} (Security: {s.get_security()})")
            print(f"     Region: {s.get_region()} | Price: {s.get_price()} FCFA")
            site_map[idx] = s
            idx += 1

    selected = []
    while not selected:
        try:
            inp = get_valid_input("Enter site number(s) (e.g., 1,3): ", lambda x: all(c.isdigit() or c==',' for c in x.replace(" ","")))
            selected = [site_map[int(i)] for i in inp.split(",") if int(i.strip()) in site_map]
            if not selected: print("No valid site selected.")
        except: print("Invalid format.")

    target_region = selected[0].get_region()

    # 3. Accommodation (Smart region mapping to prevent empty results)
    REGION_TO_HOTEL_HUB = {
        "sindou": "Banfora", "karfiguela": "Banfora", "tengrela": "Banfora", 
        "fabedougou": "Banfora", "cascades": "Banfora",
        "bala": "Bobo-Dioulasso", "dioulassoba": "Bobo-Dioulasso",
        "loropeni": "Gaoua", "tiébélé": "Gaoua", "poni": "Gaoua",
        "arli": "Fada N'Gourma", "bantia": "Fada N'Gourma",
        "oursi": "Gorom-Gorom", "gorom": "Gorom-Gorom",
        "pouni": "Po", "nazinga": "Po", "degue-degue": "Dedougou", 
        "balés": "Dedougou", "kaya": "Kaya",
        "ouagadougou": "Ouagadougou", "bazoule": "Ouagadougou", "laongo": "Ouagadougou", 
        "fespaco": "Ouagadougou", "siao": "Ouagadougou", "cathedral": "Ouagadougou",
        "bobo-dioulasso": "Bobo-Dioulasso"
    }
    
    hotel_region = REGION_TO_HOTEL_HUB.get(target_region.lower(), target_region)
    available = filter_accommodations_by_region(hotel_region)
    
    # Fallback if mapping still misses a region
    if not available:
        available = ACCOMMODATION_DB
        print(f"\nShowing all accommodations (no direct match for {target_region}):")
    else:
        print(f"\nAccommodations near {target_region} (Hub: {hotel_region}):")

    acc_map = {}
    for i, acc in enumerate(available, 1):
        print(f"  {i}. ", end="")
        acc.display()
        acc_map[i] = acc

    chosen = None
    while chosen is None:
        try:
            sel = int(get_valid_input("Select number: ", lambda x: x.isdigit()))
            chosen = acc_map[sel]
        except: print("Invalid number.")

    # 4. Reservation
    print("\nFinalize Booking:")
    arr = get_valid_input("Arrival (YYYY-MM-DD): ", lambda x: len(x)==10, "Format: YYYY-MM-DD")
    dep = get_valid_input("Departure (YYYY-MM-DD): ", lambda x: len(x)==10, "Format: YYYY-MM-DD")
    pay = get_valid_input("Payment (Cash/Credit Card/Mobile Money/Bank Transfer): ", lambda x: x.title() in VALID_PAYMENTS, "Invalid mode.")

    try:
        booking = Reservation(user, chosen, arr, dep, pay.title())
        print("\nBOOKING CONFIRMED")
        print(booking.display())
        print("\n" + booking.generate_receipt())
        print("Goodbye! Thank you for using AfriTour.")
    except ValueError as e:
        print(f"Booking failed: {e}")

if __name__ == "__main__":
    main()
