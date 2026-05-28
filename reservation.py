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
        # Automatic price calculation (POLYMORPHISM)
        self.__total_price = self._calculate_price()
        self.__status = "Confirmed"

    def _calculate_price(self) -> float:
        """Calculates total price by delegating to the accommodation's polymorphic method."""
        return self.__logement.calculate_price(self.__nights)

    def cancel(self) -> bool:
        """Cancels the reservation if allowed (idempotent operation)."""
        if self.__status == "Cancelled":
            print("⚠️ This reservation is already cancelled.")
            return False
        self.__status = "Cancelled"
        print(f"✅ Reservation {self.__id} successfully cancelled.")
        return True
    def update_payment_mode(self, new_mode: str) -> bool:
        """Updates the payment mode after creation."""
        if new_mode not in self.AUTHORIZED_PAYMENT_MODES:
            print(f"⚠️ Invalid mode. Options: {self.AUTHORIZED_PAYMENT_MODES}")
            return False
        self.__payment_mode = new_mode
        print(f"✅ Payment mode updated to: {new_mode}")
        return True
        # ───────GETTERS (Encapsulation) ─────────
    def get_id(self) -> str: return self.__id
    def get_touriste(self): return self.__touriste
    def get_logement(self): return self.__logement
    def get_dates(self) -> tuple: return self.__dates
    def get_nights(self) -> int: return self.__nights
    def get_total_price(self) -> float: return self.__total_price
    def get_status(self) -> str: return self.__status
    def get_payment_mode(self) -> str: return self.__payment_mode




    
