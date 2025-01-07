from flask_login import login_required

def login_required(func):
    return login_required(func)