from flask_mail import Mail, Message
from app import mail

def send_reminder_email(email, appointment_date):
    msg = Message("Vaccination Reminder", sender="your_email", recipients=[email])
    msg.body = f"Your vaccination appointment is scheduled on {appointment_date}."
    mail.send(msg)