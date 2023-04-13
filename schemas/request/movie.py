from marshmallow import fields

from schemas.base_movie import BaseMovieSchema
from schemas.validators import MovieValidator, HallValidator


class MovieSchemaIn(BaseMovieSchema):
    pass


class MovieUpdateSchemaIn(BaseMovieSchema):
    name = fields.String(required=False)
    rating = fields.Float(required=False, validate=MovieValidator.rating_validator)
    description = fields.String(required=False)
    ticket_price = fields.Float(required=False, validate=MovieValidator.ticket_price_validator)
    hall_id = fields.Integer(required=False, validate=HallValidator.hall_id_validator)
    # ticket_count = fields.Integer(required=False)
    start_time = fields.DateTime(required=False)
    end_time = fields.DateTime(required=False)
