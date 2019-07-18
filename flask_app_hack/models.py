from game_app import app
from db import db

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    secret_number = id.Column(db.Integer)
    attempt = id.Column(db.Integer)
    guested = db.Column(db.Boolean)
