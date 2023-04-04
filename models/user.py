from db import db

from models.enums import UserRole


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    role = db.Column(db.Enum(UserRole), default=UserRole.regular, nullable=False)

    # if the customer have a stripe account, to fill up the field, if not
    # a new account will be created via the api with the provided information

    stripe_account = db.Column(db.String, nullable=True)
    tickets = db.relationship('Ticket', back_populates='user')
