Here's a comprehensive list of files and components present in the COVID-19 Vaccination Management System project:
Frontend
Templates:
index.html (homepage)
login.html (login page)
register.html (patient registration)
dashboard.html (patient dashboard)
appointments.html (appointment listing)
vaccination_reminder.html (vaccination reminder)
404.html (error page)
500.html (internal server error)
Static Files:
styles.css (global stylesheet)
script.js (JavaScript file)
Backend
Python Files:
app.py (Flask app initialization)
models.py (database schema definitions)
routes.py (URL routing and request handling)
utils/validation.py (validation logic)
utils/email.py (email utility functions)
utils/authentication.py (authentication functions)
config.py (configuration settings)
Database:
SQLite database (default)
PostgreSQL database (optional)
Dependencies
Flask:
Flask (web framework)
Flask-SQLAlchemy (database ORM)
Flask-Login (user authentication)
Flask-Mail (email utility)
Python Libraries:
Werkzeug (password hashing)
WTForms (form validation)
Flask-WTF (form handling)
Frontend Libraries:
Bootstrap (CSS framework)
jQuery (JavaScript library)
Features
User Management:
Patient registration
Login/Logout functionality
Password hashing and verification
Vaccination Management:
Vaccination appointment scheduling
Vaccination record management
Vaccination reminder system
Appointment Management:
Appointment scheduling
Appointment listing
Email Notifications:
Vaccination reminders
Appointment reminders
Validation and Error Handling:
Form validation
Error handling and logging

# COVID-19 Vaccination Management System

A web-based application for managing COVID-19 vaccination appointments and records.

## Features

* Patient registration and login functionality
* Vaccination appointment scheduling and reminders
* Vaccination record management
* Email notifications for appointments and reminders
* Validation and error handling

## Requirements

See [requirements.txt](requirements.txt) for dependencies.

## Installation

1. Clone repository: `git clone https://github.com/your-repo/covid-vaccination-system.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run application: `flask run`

## Usage

1. Register as a patient or login existing account
2. Schedule vaccination appointment
3. View appointment details and vaccination records
4. Receive email reminders for upcoming appointments

## Contributing

Contributions welcome! Fork repository, make changes, and submit pull request.

## License

MIT License