from app import db
from flask_login import UserMixin

class Patient(db.Model, UserMixin):
    # existing code

class Vaccination(db.Model):
    # existing code

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    appointment_date = db.Column(db.DateTime, nullable=False)