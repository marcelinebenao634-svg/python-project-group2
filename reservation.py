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
