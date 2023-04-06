from db import db
from models import Ticket, Movie


class TicketManager:

    @staticmethod
    def create_ticket(data):
        ticket = Ticket(**data)
        db.session.add(ticket)
        db.session.commit()
        return ticket

    @staticmethod
    def set_ticket_price(movie_id):
        movie = Movie.query.filter_by(id=movie_id).first()
        return movie.ticket_price

    @staticmethod
    def confirm_payment(ticket):
        ticket = Ticket.query.filter_by(id=ticket.id).first()
        ticket.is_paid = True
        db.session.commit()
        return ticket

    @staticmethod
    def get_user_tickets(user):
        tickets = Ticket.query.filter_by(user_id=user.id).all()
        return tickets

