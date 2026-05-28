from person import Person, Tourist, Employee

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

from logement import Logement, Hotel, Auberge
print("what type of accomodation do you want?")
print("1. Hotel")
print("2. Auberge")
type_choice = input("Enter your choice (1 or 2): ")
if type_choix == "1":
  print("Available hotels: ")
  for i, hotel in enumerate(hotels, 1):
    print(f"{i}. {hotel.get_name()} - {hotel.get_localisation()} - {hotel.get_cost() FCFA ")}
  choice = int(input("Enter number: ")) - 1
  h = hotels[choice]
  h.display()

  elif type_choix == "2":
  print("\nAvailable auberges: ")
  for i, hotel in enumerate(auberges, 1):
    print(f"{i}. {auberge.get_name()} - {auberge.get_localisation()} - {auberge.get_cost() FCFA ")}
  choice = int(input("Enter number: ")) - 1
  a = auberges[choice]
  a.display()        

                    
