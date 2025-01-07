from flask_sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)

def init_db():
    db.create_all()

def drop_db():
    db.drop_all()