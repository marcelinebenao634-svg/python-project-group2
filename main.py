from person import Person, Tourist, Employee
from logement import Logement, Hotel, Auberge

name = input("Enter your name :")
firstname = input("Enter your firstname : ")
contact = input("Enter your contact : ")

p = Person(name, firstname, contact)
print(p.display())

t = Tourist(name, firstname, contact)
preference = input("Enter your preferences (separated by comma): ")
preferences_list = preference.split(" , ")
for pref in preferences_list:
  t.add_preference(pref.strip())
print(t.display())

post = input("Enter your post: ")
salary = input("Enter your salary: ")
e = Employee(name, firstname, contact, post, salary)
print(e.display())

name = input("Enter hotel's name : ")
localisation = input("Enter the localisation : ")
cost = input("Enter the cost : ")
stars = input("Enter the number of stars : ")
services = input("Enter the services : ")
cost = int(cost)
stars = int(stars)
services = services.split(",")
h = Hotel(name, localisation, cost, stars, services)
h.display()

name = input("Enter auberge's name : ")
localisation = input("Enter the localisation : ")
cost = input("Enter the cost : ")
type_dormitory = input("Enter the type of dormitory : ")
cost = int(cost)
a = Hotel(name, localisation, cost, type_dormitory)
a.display()
