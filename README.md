FlightBooker is a Django-based web application designed to manage flight operations, airports, and passenger bookings. The application features a clean admin interface and dynamic user views for handling flights, viewing details, and booking passengers.

Features
Flight Management: View, list, and manage flights with details including origin, destination, and duration.

Airport Directory: Maintain an up-to-date listing of airports with code and city information.

Passenger Booking: Enable booking of passengers on flights, displaying both confirmed passengers and potential candidates.

Admin Customization: Django admin integration for efficient model management and streamlined updates.

Responsive Layout: Clean HTML templates with reusable layout elements and integrated static styling.

Technology Stack
Backend: Django, Python

Frontend: HTML, CSS (using Django's static files framework)

Database: SQLite (default, can be configured for other databases)

Version Control: Git and GitHub
Project Structure
Models:

Airport: Contains airport code and city details.

Flights: Stores flight details including origin, destination, and duration (with foreign keys to Airport).

Passenger: Maintains a list of passengers and allows many-to-many relationships with flights.

Views:

flights: Displays a list of all available flights.

flight: Shows details for a specific flight including its passengers and available (non-booked) passengers.

book: A view intended for booking a passenger on a flight.

Templates:

A base layout template (layout.html) provides consistent styling and navigation across the site.

Other templates extend the base layout for flight listings, flight details, and booking functionality.

Admin Interface
The Django admin is configured to manage Flights, Airport, and Passenger models efficiently:

Custom Admin for Flights:
A custom admin class lists key attributes like flight ID, origin, destination, and duration for easy management in the admin panel.
