from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mail import Mail, Message
from utils.validation import validate_name, validate_email, validate_phone, validate_password
from utils.email import send_email
from models import Patient, Vaccination, Appointment
from forms import PatientRegistrationForm, LoginForm, VaccinationAppointmentForm

app = Flask(__name__)
app.config.from_object("config.Config")
db = SQLAlchemy(app)
login_manager = LoginManager(app)
mail = Mail(app)

## Login Manager
@login_manager.user_loader
def load_user(patient_id):
    return Patient.query.get(int(patient_id))

## Routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register_patient():
    form = PatientRegistrationForm()
    if form.validate_on_submit():
        patient = Patient(
            name=form.name.data,
            email=form.email.data,
            phone=form.phone.data,
            password=generate_password_hash(form.password.data)
        )
        db.session.add(patient)
        db.session.commit()
        flash("Registration successful!", "success")
        return redirect(url_for("login"))
    return render_template("register.html", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        patient = Patient.query.filter_by(email=form.email.data).first()
        if patient and check_password_hash(patient.password, form.password.data):
            login_user(patient)
            flash("Login successful!", "success")
            return redirect(url_for("dashboard"))
    return render_template("login.html", form=form)

@app.route("/dashboard")
@login_required
def dashboard():
    appointments = current_user.appointments
    vaccinations = current_user.vaccinations
    return render_template("dashboard.html", appointments=appointments, vaccinations=vaccinations)

@app.route("/appointments", methods=["GET", "POST"])
@login_required
def schedule_appointment():
    form = VaccinationAppointmentForm()
    if form.validate_on_submit():
        appointment = Appointment(
            patient_id=current_user.id,
            appointment_date=form.appointment_date.data,
            vaccine_name=form.vaccine_name.data
        )
        db.session.add(appointment)
        db.session.commit()
        flash("Appointment scheduled!", "success")
        send_email(current_user.email, "Appointment Scheduled", "appointment_scheduled")
        return redirect(url_for("dashboard"))
    return render_template("appointments.html", form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out!", "success")
    return redirect(url_for("index"))

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)