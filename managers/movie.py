from werkzeug.exceptions import NotFound

from db import db
from managers.ticket import TicketManager
from managers.transaction import TransactionManager
from models import Movie


class MovieManager:
    @staticmethod
    def create_movie(data):
        movie = Movie(**data)
        db.session.add(movie)
        db.session.commit()
        return movie

    @staticmethod
    def get_movie(pk):
        movie = Movie.query.filter_by(id=pk).first()
        if not movie:
            raise NotFound("Movie not found")
        return movie

    @staticmethod
    def update_movie(movie_id, data):
        movie = Movie.query.filter_by(id=movie_id).first()
        Movie.query.filter_by(id=movie_id).update(data)
        db.session.refresh(movie)
        db.session.commit()
        return movie

    @staticmethod
    def delete_movie(movie_id):
        movie = Movie.query.filter_by(id=movie_id).first()
        TransactionManager.remove_transactions(movie)
        TicketManager.remove_tickets(movie)
        db.session.delete(movie)
        db.session.commit()
