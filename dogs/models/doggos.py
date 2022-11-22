from ..database.db import db

class Doggo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    age = db.Column(db.Integer)
