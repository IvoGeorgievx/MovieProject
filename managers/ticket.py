from db import db
from models import Ticket


class TicketManager:

    @staticmethod
    def create_ticket(data):
        ticket = Ticket(**data)
        db.session.add(ticket)
        db.session.commit()
        return ticket

