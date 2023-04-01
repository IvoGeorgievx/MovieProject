from marshmallow import Schema, fields


class BaseHallSchema(Schema):
    capacity = fields.Integer(required=True)