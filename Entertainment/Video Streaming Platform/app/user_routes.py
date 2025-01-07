from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import User

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/profile')
def profile():
    return render_template('profile.html')

@user_routes.route('/settings')
def settings():
    return render_template('settings.html')