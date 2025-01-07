from flask import render_template, redirect, url_for
from app import app
from models import Patient, Vaccination, Appointment
from utils.authentication import login_required

@app.route("/register", methods=["POST"])
def register_patient():
    # existing code

@app.route("/login", methods=["GET", "POST"])
def login():
    # existing code

@app.route("/dashboard")
@login_required
def dashboard():
    # existing code

@app.route("/vaccinate", methods=["POST"])
@login_required
def vaccinate_patient():
    # existing code

@app.route("/appointments")
@login_required
def view_appointments():
    appointments = Appointment.query.filter_by(patient_id=current_user.id).all()
    return render_template("appointments.html", appointments=appointments)