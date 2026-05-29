"""
reservation.py - Booking management module.
Handles creation, pricing, payment, cancellation, refund logic, and serialization.
"""
from datetime import datetime


class Reservation:
    """Represents a booking linking a Tourist to an Accommodation."""
    _id_counter = 1000
    AUTHORIZED_PAYMENT = ("Cash", "Credit Card", "Mobile Money", "Bank Transfer")

    def __init__(self, tourist, accommodation, arrival_date: str, departure_date: str, payment_mode: str = "Mobile Money"):
        if not tourist or not accommodation:
            raise ValueError("Tourist and accommodation are required.")

        self.__id = f"RES-{Reservation._id_counter}"
        Reservation._id_counter += 1
        self.__tourist = tourist
        self.__accommodation = accommodation

        # Date validation
        try:
            self.__arrival = datetime.strptime(arrival_date, "%Y-%m-%d")
            self.__departure = datetime.strptime(departure_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")
        if self.__departure <= self.__arrival:
            raise ValueError("Departure date must be strictly after arrival date.")

        # Immutable tuple for dates
        self.__dates = (self.__arrival.strftime("%Y-%m-%d"), self.__departure.strftime("%Y-%m-%d"))
        self.__nights = (self.__departure - self.__arrival).days

        # Payment validation
        if payment_mode not in self.AUTHORIZED_PAYMENT:
            raise ValueError(f"Invalid payment mode. Choose from: {self.AUTHORIZED_PAYMENT}")
        self.__payment_mode = payment_mode

        # Automatic pricing (POLYMORPHISM)
        self.__total_price = self._calculate_price()
        self.__status = "Confirmed"

    def _calculate_price(self) -> float:
        """Delegates pricing to the accommodation's polymorphic method."""
        return self.__accommodation.calculate_price(self.__nights)

    def cancel(self) -> bool:
        """Idempotent cancellation."""
        if self.__status == "Cancelled":
            return False
        self.__status = "Cancelled"
        return True

    def calculate_refund(self) -> float:
        """Calculates refund amount based on days remaining before arrival."""
        if self.__status != "Cancelled":
            return 0.0
        days_before = (self.__arrival.date() - datetime.now().date()).days
        if days_before > 7:
            return self.__total_price          # Full refund (>7 days)
        elif days_before > 3:
            return self.__total_price * 0.5    # 50% refund (3-7 days)
        else:
            return 0.0                         # No refund (<3 days)

    def update_payment_mode(self, new_mode: str) -> bool:
        """Updates payment method safely."""
        if new_mode not in self.AUTHORIZED_PAYMENT:
            return False
        self.__payment_mode = new_mode
        return True

    # ───────── GETTERS ─────────
    def get_id(self) -> str: return self.__id
    def get_status(self) -> str: return self.__status
    def get_dates(self) -> tuple: return self.__dates
    def get_nights(self) -> int: return self.__nights
    def get_payment_mode(self) -> str: return self.__payment_mode
    def get_total_price(self) -> float: return self.__total_price
    def get_tourist(self): return self.__tourist
    def get_accommodation(self): return self.__accommodation

    # ───────── DISPLAY & RECEIPT ─────────
    def display(self) -> str:
        return (f"Reservation {self.__id} | "
                f"Tourist: {self.__tourist.get_first_name()} {self.__tourist.get_last_name()} | "
                f"Accommodation: {self.__accommodation.get_name()} | "
                f"Dates: {self.__dates[0]} to {self.__dates[1]} ({self.__nights} nights) | "
                f"Payment: {self.__payment_mode} | "
                f"Status: {self.__status} | "
                f"Total: {self.__total_price:.2f} FCFA")

    def generate_receipt(self) -> str:
        """Generates a structured digital receipt for printing or file export."""
        return (f"{'='*50}\n"
                f"  AFRI TOUR - OFFICIAL RECEIPT\n"
                f"{'='*50}\n"
                f"Reference: {self.__id}\n"
                f"Tourist: {self.__tourist.get_first_name()} {self.__tourist.get_last_name()}\n"
                f"Contact: {self.__tourist.get_contact()}\n"
                f"Accommodation: {self.__accommodation.get_name()} ({self.__accommodation.get_location()})\n"
                f"Check-in: {self.__dates[0]} | Check-out: {self.__dates[1]}\n"
                f"Nights: {self.__nights} | Payment: {self.__payment_mode}\n"
                f"Total Amount: {self.__total_price:.2f} FCFA\n"
                f"Status: {self.__status}\n"
                f"{'='*50}\n"
                f"Thank you for choosing AfriTour. Safe travels!\n")

    def __str__(self) -> str: return self.display()

    def to_dict(self) -> dict:
        """Exports reservation data to a dictionary for file I/O."""
        return {
            "id": self.__id, "status": self.__status, "payment_mode": self.__payment_mode,
            "arrival_date": self.__dates[0], "departure_date": self.__dates[1],
            "total_price": self.__total_price
        }


# ───────── EXTERNAL UTILITIES ─────────
def filter_reservations(reservations: list, status: str) -> list:
    """Returns a new list containing only reservations with the specified status."""
    return [r for r in reservations if r.get_status() == status]
