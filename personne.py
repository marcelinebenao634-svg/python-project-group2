"""
personne.py - Base Person class and its subclasses.
Demonstrates inheritance, encapsulation, and polymorphic display.
"""

class Person:
    """Base class for all individuals in the system."""
    def __init__(self, last_name, first_name, contact):
        self.__last_name = last_name
        self.__first_name = first_name
        self.__contact = contact

    def get_last_name(self): return self.__last_name
    def get_first_name(self): return self.__first_name
    def get_contact(self): return self.__contact

    def display(self):
        return f"{self.__first_name} {self.__last_name} | Contact: {self.__contact}"


class Tourist(Person):
    """Tourist subclass with travel preferences and booking history."""
    def __init__(self, last_name, first_name, contact, preferences=None):
        super().__init__(last_name, first_name, contact)
        self.__preferences = preferences if preferences is not None else []
        self.__booking_history = []

    def add_preference(self, preference):
        self.__preferences.append(preference)

    def get_preferences(self):
        return self.__preferences

    def add_to_history(self, reservation_id):
        self.__booking_history.append(reservation_id)

    def display(self):
        prefs = ", ".join(self.__preferences) if self.__preferences else "None"
        return f"Tourist: {super().display()} | Preferences: {prefs}"


class Employee(Person):
    """Employee subclass with position and salary."""
    def __init__(self, last_name, first_name, contact, position, salary):
        super().__init__(last_name, first_name, contact)
        self.__position = position
        self.__salary = salary

    def get_position(self): return self.__position
    def get_salary(self): return self.__salary

    def display(self):
        return f"Employee: {super().display()} | Position: {self.__position} | Salary: {self.__salary} FCFA"
