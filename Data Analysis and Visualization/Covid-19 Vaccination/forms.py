from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateTimeField, IntegerField
from wtforms.validators import DataRequired, Length
from utils.validation import validate_name, validate_email, validate_phone, validate_password

class PatientRegistrationForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(min=3, max=100)])
    email = StringField("Email", validators=[DataRequired(), validate_email])
    phone = StringField("Phone", validators=[DataRequired(), validate_phone])
    password = PasswordField("Password", validators=[DataRequired(), validate_password])

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), validate_email])
    password = PasswordField("Password", validators=[DataRequired(), validate_password])

class VaccinationAppointmentForm(FlaskForm):
    date = DateTimeField("Date", validators=[DataRequired(), validate_date])
    time = DateTimeField("Time", validators=[DataRequired(), validate_time])
    vaccine_name = StringField("Vaccine Name", validators=[DataRequired(), validate_vaccine_name])

class VaccinationRecordForm(FlaskForm):
    patient_id = IntegerField("Patient ID", validators=[DataRequired()])
    vaccine_name = StringField("Vaccine Name", validators=[DataRequired(), validate_vaccine_name])
    dose_number = IntegerField("Dose Number", validators=[DataRequired(), validate_dose_number])