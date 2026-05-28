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

