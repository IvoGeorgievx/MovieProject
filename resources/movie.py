from flask import request
from flask_restful import Resource

from managers.auth import auth
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
        movie = MovieManager.create_movie(data)
        return MovieSchemaOut().dump(movie)

