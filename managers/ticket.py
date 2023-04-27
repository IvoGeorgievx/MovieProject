from werkzeug.exceptions import BadRequest

from db import db
from models import Ticket, Movie, Hall


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

    @staticmethod
    def set_ticket_count(hall_id):
        hall = Hall.query.filter_by(id=hall_id).first()
        ticket_count = hall.capacity
        return ticket_count

    @staticmethod
    def check_for_available_tickets(movie_id):
        movie = Movie.query.filter_by(id=movie_id).first()
        if movie.ticket_count <= 0:
            raise BadRequest("Tickets are all sold out.")
        return movie

    @staticmethod
    def set_new_ticket_count(movie_id):
        movie = Movie.query.filter_by(id=movie_id).first()
        movie.ticket_count -= 1
        db.session.add(movie)
        db.session.commit()
        return movie

    @staticmethod
    def remove_tickets(movie):
        tickets = Ticket.query.filter_by(movie_id=movie.id).all()
        for ticket in tickets:
            db.session.delete(ticket)
