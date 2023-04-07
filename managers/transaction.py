from db import db
from models import Transaction


class TransactionManager:

    @staticmethod
    def create_transaction(ticket, transaction, user):
        transaction = Transaction(
            ticket_id=ticket.id,
            payment_id=transaction,
            user_id=user.id
        )
        db.session.add(transaction)
        db.session.commit()
        return transaction
