from db import db


class Ticket(db.Model):
    __tablename__ = "ticket"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    user = db.relationship("User")
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"), nullable=False)
    movie = db.relationship("Movie", cascade="all,delete")
    ticket_price = db.Column(db.Float, nullable=False)
    is_paid = db.Column(db.Boolean, default=False, nullable=False)
