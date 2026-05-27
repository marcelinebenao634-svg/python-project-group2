"""
Reservation module for AfriTour system.
Handles booking creation, automatic price calculation, payment mode management,
cancellation logic, and data serialization for file storage.
"""
from datetime import datetime


class Reservation:
    #Represents a booking linking a Tourist to an Accommodation.
    _id_counter = 1000
    AUTHORIZED_PAYMENT_MODES = ("Cash", "Credit Card", "Mobile Money", "Bank Transfer")

    def __init__(self, touriste, logement, arrival_date: str, departure_date: str, payment_mode: str = "Mobile Money"):
        if not touriste or not logement:
            raise ValueError("Tourist and accommodation are required.")

        self.__id = f"RES-{Reservation._id_counter}"
        Reservation._id_counter += 1
        self.__touriste = touriste
        self.__logement = logement
        # Date validation
        try:
            self.__arrival = datetime.strptime(arrival_date, "%Y-%m-%d")
            self.__departure = datetime.strptime(departure_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")

        if self.__departure <= self.__arrival:
            raise ValueError("Departure date must be strictly after arrival date.")

        # Immutable tuple for dates (Python requirement)
        self.__dates = (self.__arrival.strftime("%Y-%m-%d"), self.__departure.strftime("%Y-%m-%d"))
        self.__nights = (self.__departure - self.__arrival).days

        # Payment mode validation
        if payment_mode not in self.AUTHORIZED_PAYMENT_MODES:
            raise ValueError(f"Invalid payment mode. Choose from: {self.AUTHORIZED_PAYMENT_MODES}")
        self.__payment_mode = payment_mode

