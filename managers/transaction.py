from db import db
from models import Transaction, Ticket


class TransactionManager:
    @staticmethod
    def create_transaction(ticket, payment, user):
        transaction = Transaction(
            ticket_id=ticket.id, payment_id=payment, user_id=user.id
        )
        db.session.add(transaction)
        db.session.commit()
        return transaction

    @staticmethod
    def remove_transactions(movie):
        transactions = (
            Transaction.query.join(Ticket).filter(Ticket.movie_id == movie.id).all()
        )
        for transaction in transactions:
            db.session.delete(transaction)
