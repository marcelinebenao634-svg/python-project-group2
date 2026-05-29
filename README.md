# AfriTour - Tourism Management System

A Python project simulating a travel agency dedicated to Burkina Faso. The system offers two distinct workflows: the **tourist** (trip planning) and the **employee** (data consultation and management).



## Team Roles & Responsibilities (Group 2)
* *Member 1:* Client profile management (classes/personne.py)
* *Member 2:* Accommodation management (classes/logement.py)
* *Member 3:* Directory of attractions (classes/site_touristique.py)
* *Member 4:* Cost calculation logic and ticketing (classes/reservation.py)
* *Member 5:* Main entry point (main.py)
* *Member 6:* Technical documentation (README.md)


## Features
- **Role-based routing**: The workflow automatically adapts based on the selected role.
- **Affinity-based sorting**: Sites matching the tourist's preferences are displayed first.
- **Geographic filtering**: Accommodation search by region, with automatic redirection to the nearest hotel hub.
- **Complete booking**: Dynamic pricing (hotel tax / hostel discount) and formatted receipt generation.
- **Employee Dashboard**: System statistics, keyword search, and real-time updates (site security levels, accommodation prices).
- **OOP Architecture**: Inheritance, strict encapsulation, and polymorphism for price calculation.
  
- ## ⚙️ How to Run the Project
1. Make sure you have Python 3 installed on your machine.
2. Open a terminal in the root directory of the project (mon_projet/).
3. Run the following command:
   ```bash
   python main.py

