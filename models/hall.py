from db import db


class Hall(db.Model):
    __tablename__ = 'hall'

    id = db.Column(db.Integer, primary_key=True)
    capacity = db.Column(db.Integer, nullable=False)
