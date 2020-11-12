from app import db
from werkzeug.security import generate_password_hash
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    created_on = db.Column(db.DateTime, default=datetime.utcnow())

    def __init__(self, email, password):
        self.email = email
        self.password = generate_password_hash(password)

    def __repr__(self):
        return f"<User: {self.email}>"

    def to_dict(self):
        return {'email': self.email, 'password': 'classified', 'created_on': self.created_on}
