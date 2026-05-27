from person import Person, Tourist, Employee
from logement import Logement, Hotel, Auberge

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
  if choice =="no"
    break
  preference = input("Enter  your preference: ")
  t.add_preference(preference)
print(t.display())
print(t.get_preferences())

post = input("Enter your post: ")
salary = input("Enter your salary: ")
e = Employee(name, firstname, contact, post, salary)
print(e.display())

name = input("Enter hotel's name : ")
localisation = input("Enter the localisation : ")
cost = input("Enter the cost : ")
stars = input("Enter the number of stars : ")
services = input("Enter the services : ")
services_list = []
for service in services.split(","):
  services_list.append(service.strip())
cost = int(cost)
stars = int(stars)
h = Hotel(name, localisation, cost, stars, services_list)
h.display()

name = input("Enter auberge's name : ")
localisation = input("Enter the localisation : ")
cost = input("Enter the cost : ")
type_dormitory = input("Enter the type of dormitory : ")
cost = int(cost)
a = Hotel(name, localisation, cost, type_dormitory)
a.display()
