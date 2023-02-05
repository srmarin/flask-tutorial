from db import db

class UserModel(db.Model):
    __tablename__ = "users" # Set table name in DB

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    