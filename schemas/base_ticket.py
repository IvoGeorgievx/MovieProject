from marshmallow import Schema, fields


class BaseTicketSchema(Schema):
    movie_id = fields.Integer(required=True)
