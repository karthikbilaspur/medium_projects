import re
from datetime import datetime

def validate_name(name):
    if not name or len(name) < 3 or len(name) > 100:
        return "Invalid name"

def validate_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if not re.match(pattern, email):
        return "Invalid email"

def validate_phone(phone):
    if not phone or len(phone) != 10 or not phone.isdigit():
        return "Invalid phone number"

def validate_password(password):
    if not password or len(password) < 8 or len(password) > 128:
        return "Invalid password"

def validate_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        return "Invalid date"

def validate_time(time):
    try:
        datetime.strptime(time, "%H:%M")
    except ValueError:
        return "Invalid time"

def validate_vaccine_name(name):
    if not name or len(name) < 3 or len(name) > 100:
        return "Invalid vaccine name"

def validate_dose_number(dose):
    if not dose or not dose.isdigit():
        return "Invalid dose number"