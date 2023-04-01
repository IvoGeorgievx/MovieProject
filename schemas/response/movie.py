from marshmallow import fields

from schemas.base_movie import BaseMovieSchema


class MovieSchemaOut(BaseMovieSchema):
    id = fields.Integer(required=True)
