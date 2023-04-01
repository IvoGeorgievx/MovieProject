from marshmallow import Schema, fields

from schemas.validators import rating_validator


class BaseMovieSchema(Schema):
    name = fields.String(required=True)
    rating = fields.Float(required=True, validate=rating_validator)
    description = fields.String(required=True)
    hall_id = fields.Integer(required=True)
