# AfriTour - Tourism Management System

## 1. Project Title and Description

**AfriTour** is a Python-based tourism management system designed to promote tourist destinations in Burkina Faso. The application simulates a travel agency platform with two distinct user roles:

- **Tourist**: Can browse tourist sites, specify travel preferences, search for accommodations by region, and make reservations with automatic price calculation and receipt generation.
- **Employee**: Has access to a management dashboard to view system statistics, update site security levels, modify accommodation prices, and search the database.

The system features intelligent site sorting based on user preferences, geographic filtering for accommodations, and demonstrates core Object-Oriented Programming principles including inheritance, encapsulation, and polymorphism.

---

## 2. How to Run the Project

### Prerequisites
- **Python Version**: Python 3.6 or higher
- **Required Modules**: None (uses only Python standard library)

### Installation and Execution Steps

 **Clone or download the repository**:
   ```bash
   git clone <repository-url>
   cd afriTour*
Follow the on-screen instructions:
Enter your personal information
Specify your role (Tourist or Employee)
For tourists: Add preferences (e.g., Nature, History, Culture) and type 'done' when finished
Select tourist sites from the categorized list
Choose accommodations near your selected site
Complete the booking with arrival/departure dates and payment method

3. Features

Core Functionality
Role-based user routing with distinct workflows for tourists and employees
Preference-based site sorting - sites matching user preferences appear first
Geographic accommodation filtering with intelligent region mapping
Dynamic pricing calculation - 5% tax for hotels, 10% discount for hostels (auberges)
Formatted receipt generation with booking details
Real-time data management for employees (update security levels and prices)
Keyword search across tourist site database
Input validation with user-friendly error messages
Tourist Features
Browse 25+ tourist sites across Burkina Faso
Filter sites by category (Nature, History, Culture, Religion, Wildlife, Art)
View site details including security levels, prices, and practical tips
Make reservations with automatic price calculation
Receive formatted booking confirmation
Employee Features
View complete site and accommodation databases
Access system statistics (total sites, accommodations, security distribution)
Update site security levels (High/Medium/Low)
Modify accommodation base prices
Search sites by keyword across name, category, and description

4. Technologies Used

Programming Language: Python 3.6+
Libraries: Python Standard Library only
datetime - for date validation and calculations
Development Environment: VS Code / Terminal
Version Control: Git & GitHub

5. Project Structure

afriTour/
│
├── main.py                
├── personne.py             
├── logement.py             
├── TouristSite.py          
├── reservation.py          
└── README.md 
             
File Descriptions
main.py: Application entry point. Handles user input, role-based routing, menu display, and coordinates the booking workflow. Contains the employee dashboard interface.
personne.py: Defines the base Person class and its subclasses Tourist (with preferences and booking history) and Employee (with position and salary). Demonstrates inheritance and encapsulation.
logement.py: Contains the Accommodation base class and subclasses Hotel (with 5% tax) and Auberge (with 10% discount). Includes the complete accommodation database. Demonstrates polymorphism through the calculate_price() method.
TouristSite.py: Defines the TouristSite class with automatic region extraction and security level assignment. Contains the database of 25 tourist sites across Burkina Faso with detailed information.
reservation.py: Manages booking creation, price calculation, receipt generation, and includes cancellation/refund logic. Validates dates and payment methods.

6. OOP Structure

Class Hierarchy
Person (Base Class)
Purpose: Represents any individual in the system
Attributes: last_name, first_name, contact
Main Methods:
get_last_name(), get_first_name(), get_contact()
display() - returns formatted string
Tourist (Inherits from Person)
Purpose: Represents a tourist user with travel preferences
Additional Attributes: preferences (list), booking_history (list)
Main Methods:
add_preference(preference) - adds travel preference
get_preferences() - returns tuple of preferences
add_to_history(reservation_id) - records booking
display() - shows tourist info with preferences
Employee (Inherits from Person)
Purpose: Represents an employee with management access
Additional Attributes: position, salary
Main Methods:
get_position(), get_salary()
display() - shows employee info with position
Accommodation (Base Class)
Purpose: Represents any tourist lodging
Attributes: name, location, base_price
Main Methods:
get_name(), get_location(), get_base_price()
calculate_price(nights) - base calculation
display() - shows accommodation info
Hotel (Inherits from Accommodation)
Purpose: Represents a hotel with stars and services
Additional Attributes: stars, services
Main Methods:
get_stars(), get_services()
calculate_price(nights) - applies 5% tax
display() - shows hotel details
Auberge (Inherits from Accommodation)
Purpose: Represents a hostel with dormitory type
Additional Attributes: dorm_type
Main Methods:
get_dorm_type()
calculate_price(nights) - applies 10% discount
display() - shows hostel details
TouristSite
Purpose: Represents a tourist destination
Attributes: name, category, description, tips, address, hours, national_price, foreign_price, rating, region, security
Main Methods:
_extract_region(address) - extracts city from address
_assign_security(region) - assigns security level
get_name(), get_category(), get_region(), get_security(), get_price()
display_info() - shows complete site information
Reservation
Purpose: Manages booking creation and management
Attributes: id, tourist, accommodation, arrival, departure, nights, payment_mode, total_price, status
Main Methods:
_calculate_price() - delegates to accommodation
cancel() - cancels reservation
calculate_refund() - calculates refund amount
generate_receipt() - creates formatted receipt
display() - shows booking summary

7. Acknowledgments

Resources and References

Python Official Documentation: https://docs.python.org/3/
Object-Oriented Programming in Python: Course materials and tutorials
Burkina Faso Tourism Data: Public information about tourist sites, regions, and accommodations
VS Code Editor: Development environment
Learning Resources
Real Python tutorials on OOP and inheritance
Python documentation on datetime module
GitHub guides on repository management
Special Thanks
Professor and teaching assistants for guidance
Team members for collaboration and code review
Open-source community for best practices
Qwen studio
Claude 

Team Members links

https://github.com/ephraimbationo19-lgtm

https://github.com/Ursula60

https://github.com/baziegracepelagie

https://github.com/marcelinebenao634-svg

https://github.com/sidnomwendeedithbingboure

https://github.com/samoumiennadegebihoun8




 



