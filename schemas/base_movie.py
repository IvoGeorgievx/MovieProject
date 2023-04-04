from marshmallow import Schema, fields

from schemas.validators import rating_validator, ticket_price_validator


class BaseMovieSchema(Schema):
    name = fields.String(required=True)
    rating = fields.Float(required=True, validate=rating_validator)
    description = fields.String(required=True)
    ticket_price = fields.Float(required=True, validate=ticket_price_validator)
    hall_id = fields.Integer(required=True)

