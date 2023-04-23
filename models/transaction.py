from db import db


class Transaction(db.Model):
    __tablename__ = "transaction"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    user = db.relationship("User")
    ticket_id = db.Column(db.Integer, db.ForeignKey("ticket.id"), nullable=False)
    ticket = db.relationship("Ticket")
    payment_id = db.Column(db.String, nullable=False)
