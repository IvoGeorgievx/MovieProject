from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.hall import HallManager
from managers.movie import MovieManager
from models import UserRole
from schemas.request.movie import MovieSchemaIn
from schemas.response.movie import MovieSchemaOut
from utilities.decorators import permission_required, validate_schema


class Movie(Resource):
    @auth.login_required
    @permission_required(UserRole.admin)
    @validate_schema(MovieSchemaIn)
    def post(self):
        data = request.get_json()
        start_time, end_time, hall_id = data['start_time'], data['end_time'], data['hall_id']
        HallManager.check_hall_availability(start_time, end_time, hall_id)
        movie = MovieManager.create_movie(data)
        HallManager.set_hall_occupancy(start_time, end_time, hall_id)
        return MovieSchemaOut().dump(movie)

