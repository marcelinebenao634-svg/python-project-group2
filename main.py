from person import Person
from person import Tourist
from person import Employee

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
                   
