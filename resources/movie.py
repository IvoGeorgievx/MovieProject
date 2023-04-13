from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.hall import HallManager
from managers.movie import MovieManager
from managers.ticket import TicketManager
from models import UserRole, Movie
from schemas.request.movie import MovieSchemaIn, MovieUpdateSchemaIn
from schemas.response.movie import MovieSchemaOut
from utilities.decorators import permission_required, validate_schema


class CreateMovie(Resource):
    @auth.login_required
    @permission_required(UserRole.admin)
    @validate_schema(MovieSchemaIn)
    def post(self):
        data = request.get_json()
        start_time, end_time, hall_id = data['start_time'], data['end_time'], data['hall_id']
        data['ticket_count'] = TicketManager.set_ticket_count(hall_id)
        HallManager.check_hall_availability(start_time, end_time, hall_id)
        movie = MovieManager.create_movie(data)
        HallManager.set_hall_occupancy(start_time, end_time, movie.id, hall_id)
        return MovieSchemaOut().dump(movie), 201


class UpdateMovie(Resource):
    @auth.login_required
    @permission_required(UserRole.admin)
    @validate_schema(MovieUpdateSchemaIn)
    def put(self, pk):
        data = request.get_json()
        movie = MovieManager.get_movie(pk)
        MovieManager.update_movie(movie.id, data)
        return MovieSchemaOut().dump(movie), 200


class BrowseMovies(Resource):
    def get(self):
        movies = Movie.query.filter_by().all()
        return {"movies": MovieSchemaOut(many=True).dump(movies)}, 200


class DeleteMovie(Resource):
    @auth.login_required
    @permission_required(UserRole.admin)
    def delete(self, pk):
        movie = MovieManager.get_movie(pk)
        HallManager.remove_hall_occupancy(movie.id)
        MovieManager.delete_movie(movie.id)
        return None, 204
