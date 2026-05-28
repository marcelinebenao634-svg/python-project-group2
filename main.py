from Person import Person Tourist, Employee
from Logement import Hotel, Auberge
from TouristSite import TouristSite, search_site, site_list

name = input("Enter your name :")
firstname = input("Enter your firstname : ")
contact = input("Enter your contact : ")

p = Person(name, firstname, contact)
print(p.display())

t = Tourist(name, firstname, contact)
preference = input("Enter your preference: ")
t.add_preference(preference)

while True:
  choice = input("Do you want to add more preferences? (yes/no:) ")
  if choice =="no":
    break
  preference = input("Enter  your preference: ")
  t.add_preference(preference)
print(t.display())
print(t.get_preferences())

post = input("Enter your post: ")
salary = input("Enter your salary: ")
e = Employee(name, firstname, contact, post, salary)
print(e.display())


print("what type of accomodation do you want?")
print("1. Hotel")
print("2. Auberge")
type_choice = input("Enter your choice (1 or 2): ")
if type_choix == "1":
  print("Available hotels: ")
  for i, hotel in enumerate(Hotel, 1):
    print(f"{i}. {Hotel.get_name()} - {Hotel.get_localisation()} - {Hotel.get_cost()} FCFA ")
  choice = int(input("Enter number: ")) - 1
  h = Hotel[choice]
  h.display()

  elif type_choix == "2":
  print("\nAvailable auberges: ")
  for i, hotel in enumerate(Auberge, 1):
    print(f"{i}. {Auberge.get_name()} - {Auberge.get_localisation()} - {Auberge.get_cost()} FCFA ")
  choice = int(input("Enter number: ")) - 1
  a = Auberge[choice]
  a.display()        


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
      break
    print("Goodbye!")
