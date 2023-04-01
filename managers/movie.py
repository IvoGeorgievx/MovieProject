from db import db
from models import Movie


class MovieManager:

    @staticmethod
    def create_movie(data):
        movie = Movie(**data)
        db.session.add(movie)
        db.session.commit()
        return movie
