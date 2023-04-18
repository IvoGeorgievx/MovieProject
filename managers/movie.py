from werkzeug.exceptions import BadRequest, NotFound

from db import db
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
            raise NotFound('Movie not found')
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
        db.session.delete(movie)
        db.session.commit()



